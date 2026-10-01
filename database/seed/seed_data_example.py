from extensions import db

from ..models import User

# rename this file to 'seed_data.py' and then uncomment where this file is imported anywhere in the code base i.e app.py and launch the application with 'flask run'


def seed_data():
    existing = (
        db.session.execute(
            db.select(User).where(User.username == "")
        )  # Enter a username
        .scalars()
        .one_or_none()
    )
    if existing:
        return
    user = User(
        fname="",
        sname="",
        username="",
        email="",
        github="",
        linkedin="",
        password="",  # Enter the password hash and not a password
    )
    try:
        db.session.add(user)
        db.session.commit()
        return
    except Exception as e:
        print(e)
        db.session.rollback()
        return
