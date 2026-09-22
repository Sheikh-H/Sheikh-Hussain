import os

from flask import Flask
from flask_wtf.csrf import CSRFError

from config import Config
from database.models import *
from database.seed import seed_data
from extensions import csrf, db, init_cloudinary, limiter, migrate, server_session
from routes import *
from routes.error import (
    bad_request,
    csrf_error,
    forbidden_page,
    large_file,
    max_requests,
    not_allowed,
    not_found,
    server_error,
)
from security import init_security


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    limiter.init_app(app)
    server_session.init_app(app)

    init_cloudinary(app)
    init_security(app)

    app.register_blueprint(main)

    app.register_error_handler(CSRFError, csrf_error)

    app.register_error_handler(400, bad_request)
    app.register_error_handler(403, forbidden_page)
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, not_allowed)
    app.register_error_handler(429, max_requests)
    app.register_error_handler(500, server_error)
    app.register_error_handler(413, large_file)

    with app.app_context():
        db.create_all()
        seed_data()

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(
        debug=True,
        host="0.0.0.0",
        port=port,
    )
