from flask import render_template


def csrf_error(error):
    title = "400"
    return (
        render_template("error_pages/400.html", reason=error.description, title=title),
        400,
    )


def forbidden_page(error):
    title = "403"
    return render_template("error_pages/403.html", title=title), 403


def not_found(error):
    title = "404"
    return render_template("error_pages/404.html", title=title), 404


def bad_request(error):
    title = "400"
    return render_template("error_pages/400.html", title=title), 400


def not_allowed(error):
    title = "405"
    return render_template("error_pages/405.html", title=title), 405


def server_error(error):
    title = "500"
    return render_template("error_pages/500.html", title=title), 500


def max_requests(error):
    title = "429"
    return render_template("error_pages/429.html", title=title), 429


def large_file(error):
    title = "413"
    return render_template("error_pages/413.html", title=title), 413
