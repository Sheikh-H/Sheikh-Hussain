from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    current_app,
)
from sqlalchemy import select

from database.models import *
from extensions import db, limiter
from services import (
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
    page = request.args.get("page", default=1, type=int)
    query = db.select(Project).order_by(
        Project.featured.desc(), Project.completed.desc()
    )
    pagination = db.paginate(query, page=page, per_page=6, error_out=False)
    projects = pagination.items
    return render_template(
        "all-projects.html", projects=projects, title=title, pagination=pagination
    )


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


@main.route("/robots.txt")
def robots_txt():
    return send_from_directory(current_app.static_folder, "robots.txt")


