from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.orm import Session

from db.models import Link, ProhibitedDomain


def get_link_by_url(db: Session, link: str) -> Optional[Link]:
    query = select(Link).where(Link.source == link)
    return db.scalar(query)


def is_domain_prohibited(db: Session, domain: str) -> bool:
    query = select(exists(ProhibitedDomain)).where(ProhibitedDomain.domain == domain)
    return db.scalar(query)
