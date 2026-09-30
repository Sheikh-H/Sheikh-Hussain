from datetime import datetime, timezone

from flask import flash
from sqlalchemy import insert

from database.models import Project
from extensions import db
from services.validators.input_validator import validate_date, validate_input

from ..uploader import image_uploader


def fetch_top_projects() -> list[Project]:
    query = (
        db.select(Project)
        .order_by(Project.featured.desc(), Project.likes.desc(), Project.added.desc())
        .limit(4)
    )
    projects = db.session.execute(query).scalars().all()
    return list(projects)


def fetch_all_projects() -> list[Project]:
    query = db.select(Project).order_by(Project.added.desc())
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
    today = datetime.now(timezone.utc).date()
    title = validate_input(data.get("title", ""))
    description = validate_input(data.get("description", ""))
    github = validate_input(data.get("github", ""))
    live = validate_input(data.get("live", ""))
    tags = validate_input(data.get("tags", "").upper())
    tags = ", ".join(tag.strip() for tag in tags.split(",") if tag.strip())
    if len(tags.split(",")) > 4:
        flash("Please use 4 tags only!", "error")
        return False
    featured = data.get("featured", 0)
    completed = validate_date(data.get("completed", today))
    if not all([title, description, github, tags, completed]):
        flash("Please enter all required fields!", "error")
        return False
    if completed > today:
        flash("Please enter a valid date!", "error")
        return False
    projects = fetch_all_projects()
    for project in projects:
        if project.github == github:
            flash("The GitHub Repo is assigned to another project!", "error")
            return False
        if live and project.live == live:
            flash("This link is assigned to another project!", "error")
            return False
    image = data.get("image")
    if image and image.filename:
        upload_url = image_uploader(image, f"Projects/{title}")
        image_url = upload_url
    else:
        image_url = "https://placehold.co/500x500.png"
    try:
        query = insert(Project).values(
            title=title,
            description=description,
            github=github,
            live=live,
            likes=0,
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


def fetch_project_by_id(project_id: int) -> Project:
    project = db.get_or_404(Project, project_id)
    return project


def update_project(data: dict) -> bool:
    today = datetime.now(timezone.utc).replace(microsecond=0)
    project = fetch_project_by_id(data.get("project_id", 0))
    title = project.title
    description = project.description
    github = project.github
    live = project.live
    tags = project.tags
    featured = project.featured
    completed = project.completed
    image_url = project.image_url
    if data.get("title"):
        title = validate_input(data.get("title", ""))
    if data.get("description"):
        description = validate_input(data.get("description", ""))
    if data.get("github"):
        github = validate_input(data.get("github", ""))
    if data.get("live"):
        live = validate_input(data.get("live", ""))
    if data.get("tags"):
        tags = validate_input(data.get("tags", "").upper())
        tags = ", ".join(tag.strip() for tag in tags.split(",") if tag.strip())
        if len(tags.split(",")) > 4:
            flash("Please use 4 tags only!", "error")
            return False
    featured = data.get("featured")
    if data.get("completed"):
        completed = validate_date(data.get("completed", today))
    projects = fetch_all_projects()
    for item in projects:
        if item.project_id == project.project_id:
            continue
        if item.github == github:
            flash("The GitHub Repo is assigned to another project!", "error")
            return False
        if live and item.live == live:
            flash("This link is assigned to another project!", "error")
            return False
    if data.get("image"):
        image = data.get("image")
        if image and image.filename:
            upload_url = image_uploader(image, f"Projects/{title}")
            image_url = upload_url
        else:
            image_url = "https://placehold.co/500x500.png"
    try:
        project.title = title
        project.description = description
        project.github = github
        project.live = live
        project.tags = tags
        project.featured = featured
        project.completed = completed
        project.image_url = image_url
        project.updated = today
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
