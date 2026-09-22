from datetime import datetime, timezone

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db


class User(db.Model):
    __tablename__ = "Users_Table"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(
        String(), nullable=False, default="https://placehold.net/600x600.png"
    )
    fname: Mapped[str] = mapped_column(String(100), nullable=False)
    sname: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    github: Mapped[str] = mapped_column(String(), nullable=False)
    linkedin: Mapped[str] = mapped_column(String(), nullable=False)
    password: Mapped[str] = mapped_column(String(), nullable=False)
    added: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc).replace(microsecond=0),
    )
    updated: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
