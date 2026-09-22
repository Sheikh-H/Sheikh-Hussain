from flask import Blueprint, render_template, request

from extensions import limiter
from services.auth import *

admin = Blueprint("admin", __name__)


@admin.route("/admin/login", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
@logout_required
def login():
    page_title = "Admin Login"
    if request.method == "POST":
        data = request.form.to_dict()
        logged_in = login_function(data)
        if logged_in:
            session.clear()
            session.permanent = True
            session["username"] = logged_in.username
            return redirect(url_for("admin.home"))
    return render_template("home.html", page_title=page_title)


@admin.route("/admin/home", methods=["GET"])
@limiter.limit("50 per day")
@login_required
def home():
    page_title = "Admin Dashboard"
    return render_template("admin-home.html", page_title=page_title)
