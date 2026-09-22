from database.models import Skill
from extensions import db


def fetch_all_skills() -> list[Skill]:
    query = db.select(Skill).order_by(Skill.added.desc())
    skills = db.session.execute(query).scalars().all()
    return list(skills)
