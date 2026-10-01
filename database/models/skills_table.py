from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db


class Skill(db.Model):
    __tablename__ = "Skills_Table"
    skill_id: Mapped[int] = mapped_column(primary_key=True)
    skill: Mapped[str] = mapped_column(String(10), nullable=False)
    description: Mapped[str | None] = mapped_column(String(), nullable=True)
    duration: Mapped[int] = mapped_column(Integer(), nullable=False)
    added: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc).replace(microsecond=0),
    )
    updated: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
