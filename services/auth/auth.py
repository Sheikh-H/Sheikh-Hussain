from functools import wraps

from argon2 import PasswordHasher
from flask import flash, redirect, session, url_for

from database.models import User
from extensions import db
from services.validators import *
from services.validators.input_validator import validate_password, validate_username

verifier = PasswordHasher().verify


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = session.get("username")
        if not user:
            session.clear()
            session.permanent = True
            flash("Login to view!", "error")
            return redirect(url_for("main.home"))
        if user:
            query = db.select(User).where(User.username == user)
            user = db.session.execute(query).scalars().one_or_none()
            if not user:
                flash("Login to view!", "error")
                return redirect(url_for("main.home"))
        return f(*args, **kwargs)

    return decorated_function


def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username"):
            flash("Please Logout!", "error")
            return redirect(url_for("admin.home"))
        return f(*args, **kwargs)

    return decorated_function


def login_function(data: dict[str, str]) -> User | bool:
    valid_username = validate_username(data["username"])
    valid_password = validate_password(data["password"])
    if not valid_username or not valid_password:
        return False
    query = db.select(User).where(User.username == valid_username)
    user = db.session.execute(query).scalars().one_or_none()
    if not user:
        return False
    try:
        verifier(hash=user.password, password=valid_password)
        return user
    except Exception as e:
        print(e)
        return False
