from extensions import db

from ..models import User


def seed_data():
    existing = (
        db.session.execute(db.select(User).where(User.username == "sheikh-hussain"))
        .scalars()
        .one_or_none()
    )
    if existing:
        return
    user = User(
        fname="Sheikh",
        sname="Hussain",
        username="sheikh-hussain",
        email="sheikh.hussain1155@gmail.com",
        github="https://github.com/Sheikh-H",
        linkedin="https://linkedin.com/in/sheikh-hussain",
        password="$argon2id$v=19$m=65536,t=3,p=4$APj6oKvj6AaVb4hbDHef3A$sc1Kg1YFSQY47bbJbyiOBl9OrKovucVecbjURbrzFMw",
    )
    try:
        db.session.add(user)
        db.session.commit()
        return
    except Exception as e:
        print(e)
        db.session.rollback()
        return
