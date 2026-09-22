from database.models import Project
from extensions import db


def fetch_all_projects() -> list[Project]:
    query = db.select(Project).order_by(Project.added.desc(), Project.featured.desc())
    projects = db.session.execute(query).scalars().all()
    return list(projects)
