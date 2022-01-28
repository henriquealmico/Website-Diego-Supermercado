from flask import Blueprint
from app.encarte.controller import EncarteG, EncarteId

encarte_api = Blueprint('encarte_api', __name__)

encarte_api.add_url_rule('/encarte', view_func = EncarteG.as_view('encarte_geral'), methods = ['POST', 'GET'])

encarte_api.add_url_rule('/encarte/<int:id>', view_func = EncarteId.as_view('encarte_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])