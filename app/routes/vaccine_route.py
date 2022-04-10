from flask import Blueprint
from app.controllers import vaccine_controller


bp = Blueprint('vaccines', __name__, url_prefix="/vaccinations")

bp.post('')(vaccine_controller.create)
bp.get('')(vaccine_controller.retrieve_all)