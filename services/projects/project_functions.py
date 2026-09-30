from sqlalchemy import insert

from database.models import Project
from extensions import db
from services.validators.input_validator import validate_date, validate_input

from ..uploader import image_uploader

from datetime import datetime

def fetch_top_projects() -> list[Project]:
    query = (
        db.select(Project)
        .order_by(Project.added.desc(), Project.featured.desc())
        .limit(4)
    )
    projects = db.session.execute(query).scalars().all()
    return list(projects)


def fetch_all_projects() -> list[Project]:
    query = db.select(Project).order_by(
        Project.featured.desc(), Project.completed.desc()
    )
    projects = db.session.execute(query).scalars().all()
    return list(projects)


def fetch_all_likes() -> int:
    query = db.select(Project)
    projects = db.session.execute(query).scalars().all()
    count = 0
    for project in projects:
        count += project.likes
    return count


def insert_new_project(data: dict) -> bool:
    title = validate_input(data.get("title", ""))
    description = validate_input(data.get("description", ""))
    github = validate_input(data.get("github", ""))
    live = validate_input(data.get("link", ""))
    tags = validate_input(data.get("tags", "").rstrip(",").strip().upper())
    featured = data.get("featured", 0)
    completed = validate_date(data.get("completed", ""))
    if not all([title, description, github, live, tags, completed]):
        return False
    image_url = "https://placehold.net/500x500.png"
    if data.get("image"):
        image_url = image_uploader(data.get("image"), f"Projects/{title}")
        if image_url is None:
            image_url = ""
    try:
        query = insert(Project).values(
            title=title,
            description=description,
            github=github,
            live=live,
            tags=tags,
            featured=featured,
            completed=completed,
            image_url=image_url,
        )
        db.session.execute(query)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
