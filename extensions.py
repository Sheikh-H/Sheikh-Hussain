import cloudinary
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask_session import Session

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
server_session = Session()
limiter = Limiter(
    key_func=get_remote_address, default_limits=["1000 per day", "100 per hour"]
)


def init_cloudinary(app):
    cloudinary.config(
        cloud_name=app.config["CLOUDINARY_CLOUD_NAME"],
        api_key=app.config["CLOUDINARY_API_KEY"],
        api_secret=app.config["CLOUDINARY_API_SECRET"],
        secure=True,
    )
