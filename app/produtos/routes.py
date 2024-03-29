from flask import Blueprint
from app.produtos.controller import ProdutoG, ProdutoId

produto_api = Blueprint('produto_api', __name__)

produto_api.add_url_rule('/produto', view_func = ProdutoG.as_view('produto_geral'), methods = ['POST', 'GET'])

produto_api.add_url_rule('/produto/<int:id>', view_func = ProdutoId.as_view('produto_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
