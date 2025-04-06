from datetime import datetime, date

from sqlalchemy import String, DateTime, Date, func, event, BigInteger, Index
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from src.conf import constants


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(
        String(constants.NAME_MAX_LENGTH), nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        String(constants.NAME_MAX_LENGTH), nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(constants.EMAIL_MAX_LENGTH), nullable=True
    )
    phone: Mapped[int] = mapped_column(BigInteger, nullable=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(
        String(constants.DESCRIPTION_MAX_LENGTH), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


Index("Contacts_birth_date_idx", Contact.birth_date)


@event.listens_for(Contact, "before_insert")
async def validate_contact(mapper, connection, target):
    """Validate that Phone or Email or both are seted"""
    if target.email is None and target.phone is None:
        raise ValueError("Phone or Email must be declared")
