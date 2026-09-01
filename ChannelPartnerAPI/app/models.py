from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class ChannelPartner(Base):
    __tablename__ = "channel_partner"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending"
    )

    person_of_contact: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    mobile: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    members: Mapped[list["ChannelPartnerMember"]] = relationship(
        back_populates="channel_partner"
    )


class ChannelPartnerMember(Base):
    __tablename__ = "channel_partner_member"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    channel_partner_id: Mapped[int] = mapped_column(
        ForeignKey("channel_partner.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    mobile: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    designation: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="active"
    )

    channel_partner: Mapped["ChannelPartner"] = relationship(
        back_populates="members"
    )