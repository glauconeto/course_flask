from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    DebugToolbarExtension(app)
    if app.debug:
        DebugToolbarExtension(app)