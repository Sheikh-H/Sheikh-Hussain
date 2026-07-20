from datetime import timedelta
from flask_session import Session
import secrets
from flask import (
    Flask,
    render_template,
    request,
    session,
    abort,
    redirect,
    url_for,
    flash,
    Response,
)
from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.uploader
from services.database import (
    get_skills,
    insert_skill,
    get_projects,
    insert_project,
    get_skill,
    update_project,
    update_skill,
    delete_skill,
    get_project,
    delete_project,
    get_user,
    search_projects,
    all_tags,
)
from services.auth import login_user, login_required, csrf_required

load_dotenv()

app = Flask(__name__)

# Take off later - Only used during development
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Uploading project images to online platform
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)


# session management:
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="LAX",
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=15),
)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

Session(app)


@app.route("/", methods=["GET"])
def home():
    skills = get_skills()
    projects = get_projects(5)
    return render_template("pages/home.html", skills=skills, projects=projects)


@app.route("/projects")
def all_projects():
    title = "All Projects"
    tags = all_tags()
    search = request.args.get("search", "").strip().lower()
    tag = request.args.get("tags", "").strip().lower()
    projects = search_projects(search, tag)
    return render_template(
        "pages/projects.html", title=title, projects=projects, tags=tags
    )


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    if session.get("token"):
        return redirect(url_for("admin"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if not username:
            flash("Please enter a username", "error")
            return redirect(url_for("login"))
        if not password:
            flash("Please enter a password", "error")
            return redirect(url_for("login"))
        success = login_user(username, password)
        if success:
            session.clear()
            session.permanent = True
            user = get_user()
            if not user:
                flash("Unable to login, try again", "error")
                return redirect(url_for("login"))
            session["token"] = user["id"]
            session["csrf_token"] = secrets.token_hex(32)
            flash("Login Successful", "success")
            return redirect(url_for("admin"))
        flash("Login Unsuccessful", "error")
        return redirect(url_for("login"))
    return render_template("pages/admin/login.html")


@app.route("/admin/dashboard", methods=["GET"])
@login_required
def admin():
    title = "Admin Panel"
    return render_template("pages/admin/admin_panel.html", title=title)


@app.route("/admin/add-project", methods=["GET", "POST"])
@login_required
def add_project():
    if request.method == "POST":
        csrf_required()
        project_title = str(request.form.get("title")).lower()
        description = request.form.get("description").strip().lower()
        completion = request.form.get("completion")
        image = request.files.get("image")
        image_url = "https://placehold.co/250x150"
        if image and image.filename:
            try:
                upload_image = cloudinary.uploader.upload(
                    image, folder="project_images"
                )
                image_url = upload_image["secure_url"]
            except Exception as e:
                print(e)
                flash("Unable to upload image, try again", "error")
                return redirect(url_for("add_project"))
        tags = str(request.form.get("tags")).lower().replace(" ", "").strip(",")
        github = request.form.get("github")
        demo = request.form.get("demo")
        featured = request.form.get("featured")
        featured = 1 if request.form.get("featured") else 0
        new_project = {
            "title": project_title,
            "description": description,
            "completion": completion,
            "image_url": image_url,
            "tags": tags,
            "github": github,
            "demo": demo,
            "featured": featured,
        }
        success = insert_project(new_project)
        if success:
            flash("New Project Added", "success")
            return redirect(url_for("admin"))
        flash("Unable to add project", "error")
        return redirect(url_for("add_project"))
    return render_template("pages/admin/add_project.html")


@app.route("/admin/add-skill", methods=["GET", "POST"])
@login_required
def add_skill():
    skills = get_skills()
    if request.method == "POST":
        csrf_required()
        new_skill = str(request.form.get("skill")).strip().lower()
        new_progress = str(request.form.get("progress")).strip(" ").lower()
        for skill in skills:
            if skill["skill"].lower() == new_skill:
                abort(400)
        success = insert_skill(new_skill, new_progress)
        if success:
            flash("New skill has been added!", "success")
            return redirect(url_for("admin"))
        flash("Unable to add skill", "error")
        return redirect(url_for("add_skill"))
    return render_template("pages/admin/add_skill.html")


@app.route("/admin/skills", methods=["GET", "POST"])
@login_required
def admin_skills():
    skills = get_skills()
    if request.method == "POST":
        csrf_required()
        skill = request.form.get("skill-id")
        return redirect(url_for("modify_skill", id=skill))
    return render_template("pages/admin/skills.html", skills=skills)


@app.route("/admin/modify-skill/<int:id>", methods=["GET", "POST"])
@login_required
def modify_skill(id):
    skill = get_skill(id)
    if not skill:
        flash("Skill not found", "error")
        return redirect(url_for("admin_skills"))
    if request.method == "POST":
        csrf_required()
        updated_skill = request.form.get("skill")
        updated_progress = request.form.get("progress")
        success = update_skill(id, updated_skill, updated_progress)
        if success:
            flash("Skill Modified!", "success")
            return redirect(url_for("admin_skills"))
        flash("Unable to modify skill.", "error")
        return redirect(url_for("modify_skill", id=id))
    return render_template("pages/admin/skill.html", skill=skill)


@app.route("/admin/remove-skill/<int:id>", methods=["POST"])
@login_required
def remove_skill(id):
    csrf_required()
    success = delete_skill(id)
    if success:
        flash("Skill deleted!", "success")
        return redirect(url_for("admin_skills"))
    flash("Unable to delete skill", "error")
    return redirect(url_for("admin_skills"))


@app.route("/admin/projects", methods=["GET", "POST"])
@login_required
def admin_projects():
    projects = get_projects()
    if request.method == "POST":
        csrf_required()
        project = request.form.get("project-id")
        return redirect(url_for("modify_project", id=project))
    return render_template("pages/admin/projects.html", projects=projects)


@app.route("/admin/modify-project/<int:id>", methods=["GET", "POST"])
@login_required
def modify_project(id):
    project = get_project(id)
    if not project:
        flash("Project not found", "error")
        return redirect(url_for("admin"))
    if request.method == "POST":
        csrf_required()
        project_title = str(request.form.get("title")).strip().lower()
        description = request.form.get("description").strip().lower()
        completion = request.form.get("completion")
        image = request.files.get("image")
        image_url = project["image_url"]
        if image and image.filename:
            try:
                upload_image = cloudinary.uploader.upload(
                    image, folder="project_images"
                )
                image_url = upload_image["secure_url"]
            except Exception as e:
                print(e)
                flash("Unable to upload image, try again", "error")
                return redirect(url_for("modify_project", id=id))
        tags = str(request.form.get("tags")).lower().replace(" ", "").strip(",")
        github = request.form.get("github")
        demo = request.form.get("demo")
        featured = request.form.get("featured")
        featured = 1 if request.form.get("featured") else 0
        project = {
            "id": id,
            "title": project_title,
            "description": description,
            "completion": completion,
            "image_url": image_url,
            "tags": tags,
            "github": github,
            "demo": demo,
            "featured": featured,
        }
        success = update_project(project)
        if success:
            flash("Project Modified Successfully", "success")
            return redirect(url_for("admin_projects"))
        flash("Unable to modify project.", "error")
        return redirect(url_for("modify_project", id=id))
    return render_template("pages/admin/project.html", project=project)


@app.route("/admin/remove-project/<int:id>", methods=["POST"])
@login_required
def remove_project(id):
    csrf_required()
    success = delete_project(id)
    if success:
        flash("Project removed!", "success")
        return redirect(url_for("admin_projects"))
    flash("Unable to delete project", "error")
    return redirect(url_for("remove_project", id=id))


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session.clear()
    flash("Logout Successful!", "success")
    return redirect(url_for("home"))


@app.route("/sitemap.xml")
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
    <loc>{request.url_root}</loc>
    </url>
    <url>
    <loc>{request.url_root}projects</loc>
    </url>
    </urlset>
    """
    return Response(xml, mimetype="application/xml")


@app.errorhandler(403)
def forbidden(error):
    return render_template("pages/error/403.html"), 403


@app.errorhandler(404)
def not_found(error):
    return render_template("pages/error/404.html"), 404


@app.errorhandler(400)
def bad_request(error):
    return render_template("pages/error/400.html"), 400


@app.errorhandler(500)
def server_error(error):
    return render_template("pages/error/500.html"), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
