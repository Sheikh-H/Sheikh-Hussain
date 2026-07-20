from argon2 import PasswordHasher
from dotenv import load_dotenv
from functools import wraps
from flask import session, redirect, url_for, request, abort
from services.database import get_user

load_dotenv()
hasher = PasswordHasher()


def csrf_required():
    token = request.form.get("csrf_token")
    if not token:
        abort(400)
    if token != session.get("csrf_token"):
        abort(400)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("token") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


def login_user(username, password):
    users = get_user()
    if users:
        if users["username"] == username:
            try:
                hasher.verify(users["password"], password)
                return True
            except Exception as e:
                print(e)
                return False
    else:
        return False