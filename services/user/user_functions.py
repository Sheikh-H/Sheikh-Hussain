from database.models import User
from extensions import db


def fetch_my_details() -> dict | None:
    query = db.select(User)
    user = db.session.execute(query).scalars().first()
    if not user:
        return None
    sheikh = {
        "github": user.github,
        "linkedin": user.linkedin,
        "image_url": user.image_url,
        "email": user.email,
        "fname": user.fname,
        "sname": user.sname,
    }
    return sheikh
