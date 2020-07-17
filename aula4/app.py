from flask import Flask, request
import views

app = Flask(__name__)

def create_app():
    """Factory principal"""

    app = Flask(__name__)
    if testing:
        debug.init_app(app)
    views.init_app(app)
    
    return app