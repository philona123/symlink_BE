from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load routes from the controller
    from .controllers import init_routes
    init_routes(app)

    return app
