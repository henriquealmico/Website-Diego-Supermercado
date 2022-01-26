from flask import Blueprint
from app.produtos.controller import ProdutoG, ProdutoId, EncarteG, EncarteId

produto_api = Blueprint('produto_api', __name__)
encarte_api = Blueprint('encarte_api', __name__)

produto_api.add_url_rule('/produto', view_func = ProdutoG.as_view('produto_geral'), methods = ['POST', 'GET'])

produto_api.add_url_rule('/produto/<int:id>', view_func = ProdutoId.as_view('produto_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

encarte_api.add_url_rule('/encarte', view_func = EncarteG.as_view('encarte_geral'), methods = ['POST', 'GET'])

encarte_api.add_url_rule('/encarte/<int:id>', view_func = EncarteId.as_view('encarte_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])