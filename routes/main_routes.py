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
from sqlalchemy import select

from database.models import *
from extensions import db, limiter
from services import (
    fetch_all_projects,
    fetch_all_skills,
    fetch_my_details,
    fetch_top_projects,
)

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


@main.route("/add-like/<int:project_id>", methods=["POST"])
@limiter.limit("5 per day", methods=["POST"])
def add_like(project_id):
    query = select(Project).where(Project.project_id == project_id)
    project = db.session.execute(query).scalars().one_or_none()
    if not project:
        abort(404)
    try:
        project.likes += 1
        db.session.commit()
        return redirect(url_for("main.all_projects"))
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for("main.all_projects"))
