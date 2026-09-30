from datetime import datetime, timezone

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from database.models import *
from extensions import limiter
from services.auth import *
from services.projects import *
from services.skills import *

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
            flash("Login Successful!", "success")
            return redirect(url_for("admin.home"))
        else:
            flash("Unable to login, try again!", "error")
            return redirect(url_for("admin.login"))
    return render_template("admin/login.html", page_title=page_title)


@admin.route("/admin/logout", methods=["POST"])
@limiter.limit("5 per day", methods=["POST"])
@login_required
def logout():
    session.clear()
    session.permanent = True
    flash("Logging out!", "success")
    return "", 204


@admin.route("/admin/home", methods=["GET"])
@limiter.limit("50 per day")
@login_required
def home():
    title = "Admin Page"
    likes = fetch_all_likes()
    projects = len(fetch_all_projects())
    return render_template(
        "admin/admin-home.html", title=title, likes=likes, projects=projects
    )


@admin.route("/admin/add-project", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
@login_required
def add_project():
    title = "Add Project"
    today = datetime.now(timezone.utc).date()
    if request.method == "POST":
        data = request.form.to_dict()
        data["image"] = (
            request.files.get("image") if request.files.get("image") else None
        )
        data["featured"] = 1 if request.form.get("featured") == "on" else 0
        added = insert_new_project(data)
        if added:
            flash("New project added!", "success")
            return redirect(url_for("admin.home"))
        else:
            flash("Unable to add project!", "error")
            return redirect(url_for("admin.add_project"))
    return render_template("admin/add-project.html", title=title, today=today)


@admin.route("/admin/all-projects", methods=["GET"])
@login_required
def all_projects():
    title = "All Projects"
    page = request.args.get("page", default=1, type=int)
    query = db.select(Project).order_by(Project.added.desc())
    pagination = db.paginate(query, per_page=6, page=page, error_out=False)
    projects = pagination.items
    return render_template(
        "admin/all-projects.html", title=title, projects=projects, pagination=pagination
    )


@admin.route("/admin/project/<int:project_id>", methods=["GET", "POST"])
@limiter.limit("10 per day", methods=["POST"])
@login_required
def project_page(project_id):
    project = fetch_project_by_id(project_id)
    title = f"Project: {project.title.upper()}"
    if request.method == "POST":
        data = request.form.to_dict()
        image = request.files.get("image") if request.files.get("image") else None
        data["image"] = image
        data["featured"] = 1 if request.form.get("featured") == "on" else 0
        data["project_id"] = project_id
        updated = update_project(data)
        if updated:
            flash("Project updated!", "success")
            return redirect(url_for("admin.project_page", project_id=project_id))
        else:
            flash("Unable to update!", "error")
            return redirect(url_for("admin.project_page", project_id=project_id))
    return render_template("admin/project-view.html", title=title, project=project)


@admin.route("/admin/project/<int:project_id>/delete", methods=["POST"])
@limiter.limit("3 per day", methods=["POST"])
@login_required
def delete_project(project_id):
    success = remove_project(project_id)
    if success:
        flash("Project deleted!", "success")
        return redirect(url_for("admin.all_projects"))
    flash("Unable to delete!", "error")
    return redirect(url_for("admin.project_page", project_id=project_id))


@admin.route("/admin/add-skill", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
@login_required
def add_skill():
    title = "Add new skill"
    if request.method == "POST":
        data = request.form.to_dict()
        success = add_new_skill(data)
        if success:
            flash("New skill added!", "success")
            return redirect(url_for("admin.home"))
        else:
            flash("Unable to add skill!", "error")
            return redirect(url_for("admin.add_skill"))
    return render_template("admin/add-skill.html", title=title)


@admin.route("/admin/skills", methods=["GET"])
@limiter.limit("5 per day")
@login_required
def all_skills():
    title = "All skills"
    page = request.args.get("page", default=1, type=int)
    query = db.select(Skill).order_by(Skill.added.desc())
    pagination = db.paginate(query, per_page=3, page=page, error_out=False)
    skills = pagination.items
    return render_template(
        "admin/all-skills.html", title=title, skills=skills, pagination=pagination
    )


@admin.route("/admin/skill/<int:skill_id>", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
@login_required
def skill_page(skill_id):
    skill = fetch_skill_by_id(skill_id)
    title = f"Skill: {skill.skill.upper()}"
    if request.method == "POST":
        data = request.form.to_dict()
        data["skill_id"] = skill_id
        success = update_a_skill(data)
        if success:
            flash("Skill updated!", "success")
            return redirect(url_for("admin.skill_page", skill_id=skill_id))
        flash("Unable to update skill!", "error")
        return redirect(url_for("admin.skill_page", skill_id=skill_id))
    return render_template("admin/update-skill.html", title=title, skill=skill)
