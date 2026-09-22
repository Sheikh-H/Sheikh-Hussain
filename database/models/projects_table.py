from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db


class Project(db.Model):
    __tablename__ = "Projects_Table"
    project_id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str | None] = mapped_column(
        String(), nullable=True, default="https://placehold.net/600x600.png"
    )
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    markdown: Mapped[str | None] = mapped_column(String(), nullable=True)
    github: Mapped[str] = mapped_column(String(), nullable=False)
    live: Mapped[str | None] = mapped_column(String(), nullable=True)
    tags: Mapped[str | None] = mapped_column(String(), nullable=True)
    featured: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    added: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc).replace(microsecond=0),
    )
    updated: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
