from sqlalchemy import select
from sqlalchemy.orm import Session
from urllib.parse import urlparse, ParseResult
import string
from app.db_api.models import Link, ProhibitedDomain

ID_SYMBOLS = string.digits + string.ascii_letters


# https://github.com/Tishka17/aiogram_dialog/blob/develop/aiogram_dialog/context/stack.py#L22
def num_to_str(int_id: int) -> str:
    if not int_id:
        return ID_SYMBOLS[0]

    base = len(ID_SYMBOLS)
    res = ""

    while int_id:
        int_id, mod = divmod(int_id, base)
        res += ID_SYMBOLS[mod]

    return res


def validate_link(link_data: ParseResult, db: Session) -> tuple[str, str]:
    link = link_data.geturl()

    if not link_data.netloc:
        return link, ''

    if link_data.scheme not in ['https', 'http']:
        return '', 'Not valid URL-scheme'
    if db.execute(select(ProhibitedDomain).where(ProhibitedDomain.domain == link_data.netloc)).first():
        return '', 'Domain is prohibited'

    if not link.endswith('/'):
        link = link + '/'

    return link, ''


def get_shortened_link(link: str, db: Session) -> tuple[str, str]:

    link_data = urlparse(link)
    link, message = validate_link(link_data, db)

    if not link:
        return link, message

    shortened_link: Link = db.execute(
        select(
            Link
        ).where(
            Link.source == link_data.geturl()
        )
    ).scalars().first()

    if shortened_link is None:
        link_number = db.execute("select count(*) from links").scalars().first()
        shortened_link = Link(source=link, cropped=num_to_str(link_number))
        db.add(shortened_link)
        db.commit()

    return shortened_link.cropped, message


def get_source(shortened: str, db: Session):
    return db.execute(
        select(
            Link
        ).where(
            Link.cropped == shortened
        )
    ).scalars().first()
