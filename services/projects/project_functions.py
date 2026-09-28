from database.models import Project
from extensions import db


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
