from flask import Blueprint
from app.cupons.controller import CupomG, CupomId

cupom_api = Blueprint('cupom_api', __name__)


cupom_api.add_url_rule('/cupom', view_func = CupomG.as_view('cupom_geral'), methods = ['POST', 'GET'])

cupom_api.add_url_rule('/cupom/<int:id>', view_func = CupomId.as_view('cupom_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

