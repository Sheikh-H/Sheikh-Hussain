from datetime import datetime, timezone

from flask import flash
from sqlalchemy import delete, insert

from database.models import Skill
from extensions import db
from services.validators.input_validator import validate_input, validate_integer


def fetch_all_skills() -> list[Skill]:
    query = db.select(Skill).order_by(Skill.added.desc())
    skills = db.session.execute(query).scalars().all()
    return list(skills)


def fetch_skill_by_id(skill_id: int) -> Skill:
    skill = db.get_or_404(Skill, skill_id)
    return skill


def add_new_skill(data: dict) -> bool:
    skills = fetch_all_skills()
    skill = validate_input(data.get("skill", ""))
    for item in skills:
        if item.skill.lower() == skill.lower():
            flash("Existing skill!", "error")
            return False
    description = validate_input(data.get("description", ""))
    duration = validate_integer(data.get("duration", 0))
    if not all([skill, duration]):
        flash("Please provide all fields!", "error")
        return False
    if duration < 1:
        flash("Please enter a valid duration!", "error")
        return False
    if duration > 36:
        flash("Please enter a valid duration!", "error")
        return False
    try:
        query = insert(Skill).values(
            skill=skill, description=description, duration=duration
        )
        db.session.execute(query)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def update_a_skill(data: dict) -> bool:
    today = datetime.now(timezone.utc).replace(microsecond=0)
    skill = fetch_skill_by_id(data.get("skill_id", 0))
    title = skill.skill
    description = skill.description
    duration = skill.duration
    if data.get("skill"):
        title = validate_input(data.get("skill", ""))
    if data.get("description"):
        description = validate_input(data.get("description", ""))
    if data.get("duration"):
        new_duration = validate_integer(data.get("duration", 0))
        if new_duration is None or new_duration < 1 or new_duration > 36:
            flash("Please enter a valid duration!", "error")
            return False
        duration = new_duration
    try:
        skill.skill = title
        skill.description = description
        skill.duration = duration
        skill.updated = today
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def remove_skill(skill_id: int) -> bool:
    skill = fetch_skill_by_id(skill_id)
    try:
        query = delete(Skill).where(Skill.skill_id == skill.skill_id)
        db.session.execute(query)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
