from flask import Blueprint, Flask
from app.routes.vaccine_route import bp as bp_vaccines

api = Blueprint("api", __name__)

def init_app(app: Flask):
    api.register_blueprint(bp_vaccines)
    app.register_blueprint(api)