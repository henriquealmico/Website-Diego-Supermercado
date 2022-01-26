from flask import Blueprint
from app.pedido.controller import CarrinhoG, CarrinhoId, PedidoG, PedidoId

carrinho_api = Blueprint('carrinho_api', __name__)
pedido_api = Blueprint('pedido_api', __name__)

carrinho_api.add_url_rule('/carrinho', view_func = CarrinhoG.as_view('carrinho_geral'), methods = ['POST', 'GET'])

carrinho_api.add_url_rule('/carrinho/<int:id>', view_func = CarrinhoId.as_view('carrinho_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

pedido_api.add_url_rule('/pedido', view_func = PedidoG.as_view('pedido_geral'), methods = ['POST', 'GET'])

pedido_api.add_url_rule('/pedido/<int:id>', view_func = PedidoId.as_view('pedido_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])