def init_security(app):
    @app.after_request
    def security_headers(response):
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' "
            "https://placehold.co "
            "https://placehold.net/ "
            "https://res.cloudinary.com/dcnpmdfzl/image/upload/; "
        )
        return response
