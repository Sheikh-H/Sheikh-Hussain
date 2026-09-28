from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)

from database.models import *
from extensions import limiter
from services import fetch_all_skills, fetch_my_details, fetch_top_projects

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    page_title = "Sheikh Hussain | Full Stack Web Developer"
    projects = fetch_top_projects()
    skills = fetch_all_skills()
    sheikh = fetch_my_details()
    return render_template(
        "home.html",
        page_title=page_title,
        projects=projects,
        skills=skills,
        sheikh=sheikh,
    )


@main.route("/all-projects", methods=["GET"])
def all_projects():
    title = "Sheikh Hussain | My Projects"
    projects = fetch_all_projects()
    return render_template("all-projects.html", projects=projects, title=title)
