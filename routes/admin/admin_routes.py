import os

from flask import Blueprint, Request, render_template, url_for
from extensions import limiter

admin = Blueprint("admin", __name__)

@admin.route("/admin-login", methods=["GET", 'POST'])
@limiter.limit("5 per day", methods=['POST'])
@logout_required
def login():
    title = ""
    return render_template("")