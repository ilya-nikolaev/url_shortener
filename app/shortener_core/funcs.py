import string
from typing import Optional
from urllib.parse import urlparse

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import Link, ProhibitedDomain
from app.shortener_core.exc import LinkNotValid

ID_SYMBOLS = string.digits + string.ascii_letters
ALPHABET_LENGTH = len(ID_SYMBOLS)


# https://github.com/Tishka17/aiogram_dialog/blob/develop/aiogram_dialog/context/stack.py#L22
def num_to_str(int_id: int) -> str:
    if not int_id:
        return ID_SYMBOLS[0]

    base = len(ID_SYMBOLS)
    res = []

    while int_id:
        int_id, mod = divmod(int_id, base)
        res.append(ID_SYMBOLS[mod])

    return "".join(res)


def str_to_num(line: str) -> int:
    return sum(ID_SYMBOLS.index(symbol) * ALPHABET_LENGTH ** i for i, symbol in enumerate(line))


def validate_link(link: str, db: Session) -> str:
    link_data = urlparse(link)
    formatted_link = link_data.geturl()

    if not link_data.netloc:
        return formatted_link

    if link_data.scheme not in ['https', 'http']:
        raise LinkNotValid('Not valid URL-scheme')
    if db.execute(select(ProhibitedDomain).where(ProhibitedDomain.domain == link_data.netloc)).first():
        raise LinkNotValid('Domain is prohibited')

    if not formatted_link.endswith('/'):
        formatted_link = formatted_link

    return formatted_link


def get_shortened_link(link: str, db: Session) -> tuple[str, str]:
    try:
        link = validate_link(link, db)
    except LinkNotValid as e:
        return "", e.message

    query = select(Link).where(Link.source == link)
    shortened_link: Link = db.scalar(query)

    if shortened_link is None:
        shortened_link = Link(source=link)
        db.add(shortened_link)
        db.commit()

    return num_to_str(shortened_link.id), ""


def get_source(shortened: str, db: Session) -> Optional[Link]:
    if len(shortened) > 42:  # protection against freezes during calculations
        return None

    try:
        link_id = str_to_num(shortened)
    except ValueError:
        return None

    query = select(Link).where(Link.id == link_id)
    return db.scalar(query)
