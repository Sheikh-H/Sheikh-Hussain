from datetime import datetime, timezone

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
from services import fetch_all_projects, fetch_all_skills

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
def home():
    page_title = "Sheikh Hussain | Full Stack Web Developer"
    projects = fetch_all_projects()
    skills = fetch_all_skills()
    sheikh = fetch_my_details()
    return render_template(
        "home.html", page_title=page_title, projects=projects, skills=skills, sheikh=sheikh
    )
