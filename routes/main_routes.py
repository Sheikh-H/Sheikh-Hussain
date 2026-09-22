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

from extensions import limiter

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@limiter.limit("5 per day", methods=["POST"])
def home():
    page_title = "Sheikh Hussain | Full Stack Web Developer"

    return render_template("", page_title=page_title)
