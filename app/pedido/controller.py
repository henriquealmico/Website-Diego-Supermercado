from app.pedido.models import Carrinho, Pedido
from flask import request, jsonify
from flask.views import MethodView



class CarrinhoG(MethodView): #/carrinho

    def post(self):

        body = request.json

        preco_total = body.get('preco_total')
        data_pedido = body.get('data_pedido')
        forma_pagamento = body.get('forma_pagamento')
        modelo_entrega = body.get('modelo_entrega')
        preco_entrega = body.get('preco_entrega')
        quantidade_itens = body.get('quantidade_itens')
        prazo_entrega = body.get('prazo_entrega')
        agendamento_entrega = body.get('agendamento_entrega')


        if  isinstance(preco_total, float) and isinstance(data_pedido, str) and isinstance(forma_pagamento, str) and\
            isinstance(modelo_entrega, str) and isinstance(preco_entrega, str) and isinstance(quantidade_itens, int) and\
            isinstance(prazo_entrega, str) and isinstance(agendamento_entrega, str):


            carrinho = Carrinho(preco_total=preco_total, data_pedido=data_pedido, forma_pagamento=forma_pagamento, modelo_entrega=modelo_entrega,\
                                preco_entrega=preco_entrega, quantidade_itens=quantidade_itens, prazo_entrega=prazo_entrega,\
                                agendamento_entrega=agendamento_entrega)

            carrinho.save()
            return carrinho.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        carrinhos = Carrinho.query.all()
        return jsonify([carrinho.json() for carrinho in carrinhos]), 200


class CarrinhoId(MethodView): #/carrinho/<int:id>

    def get(self, id):

        carrinho = Carrinho.query.get_or_404(id)
        return carrinho.json()

    def put(self, id):

        body = request.json
        carrinho = Carrinho.query.get_or_404(id)

        preco_total = body.get('preco_total')
        data_pedido = body.get('data_pedido')
        forma_pagamento = body.get('forma_pagamento')
        modelo_entrega = body.get('modelo_entrega')
        preco_entrega = body.get('preco_entrega')
        quantidade_itens = body.get('quantidade_itens')
        prazo_entrega = body.get('prazo_entrega')
        agendamento_entrega = body.get('agendamento_entrega')


        if  isinstance(preco_total, float) and isinstance(data_pedido, str) and isinstance(forma_pagamento, str) and\
            isinstance(modelo_entrega, str) and isinstance(preco_entrega, str) and isinstance(quantidade_itens, int) and\
            isinstance(prazo_entrega, str) and isinstance(agendamento_entrega, str):

            carrinho.preco_total = preco_total
            carrinho.data_pedido = data_pedido
            carrinho.forma_pagamento = forma_pagamento
            carrinho.modelo_entrega = modelo_entrega
            carrinho.preco_entrega = preco_entrega
            carrinho.quantidade_itens = quantidade_itens
            carrinho.prazo_entrega = prazo_entrega
            carrinho.agendamento_entrega = agendamento_entrega


            carrinho.update()
            return carrinho.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        carrinho = Carrinho.query.get_or_404(id)

        preco_total = body.get('preco_total', carrinho.preco_total)
        data_pedido = body.get('data_pedido', carrinho.data_pedido)
        forma_pagamento = body.get('forma_pagamento', carrinho.forma_pagamento)
        modelo_entrega = body.get('modelo_entrega', carrinho.modelo_entrega)
        preco_entrega = body.get('preco_entrega', carrinho.preco_entrega)
        quantidade_itens = body.get('quantidade_itens', carrinho.quantidade_itens)
        prazo_entrega = body.get('prazo_entrega', carrinho.prazo_entrega)
        agendamento_entrega = body.get('agendamento_entrega', carrinho.agendamento_entrega)


        if  isinstance(preco_total, float) and isinstance(data_pedido, str) and isinstance(forma_pagamento, str) and\
            isinstance(modelo_entrega, str) and isinstance(preco_entrega, str) and isinstance(quantidade_itens, int) and\
            isinstance(prazo_entrega, str) and isinstance(agendamento_entrega, str):

            carrinho.preco_total = preco_total
            carrinho.data_pedido = data_pedido
            carrinho.forma_pagamento = forma_pagamento
            carrinho.modelo_entrega = modelo_entrega
            carrinho.preco_entrega = preco_entrega
            carrinho.quantidade_itens = quantidade_itens
            carrinho.prazo_entrega = prazo_entrega
            carrinho.agendamento_entrega = agendamento_entrega

            carrinho.update()
            return carrinho.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        carrinho = Carrinho.query.get_or_404(id)
        carrinho.delete(carrinho)
        return carrinho.json()
        
        



class PedidoG(MethodView): #/pedido

    def post(self):

        body = request.json


        pagamento_confirmado = body.get('pagamento_confirmado')
        data_confirmacao_pagamento = body.get('data_confirmacao_pagamento')
        numero_parcelas = body.get('numero_parcelas')


        if  isinstance(pagamento_confirmado, bool) and isinstance(data_confirmacao_pagamento, str) and isinstance(numero_parcelas, int):

            pedido = Pedido(numero_parcelas=numero_parcelas, pagamento_confirmado=pagamento_confirmado, data_confirmacao_pagamento=data_confirmacao_pagamento)

            pedido.save()
            return pedido.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        pedidos = Pedido.query.all()
        return jsonify([pedido.json() for pedido in pedidos]), 200


class PedidoId(MethodView): #/pedido/<int:id>

    def get(self, id):

        pedido = Pedido.query.get_or_404(id)
        return pedido.json()

    def put(self, id):

        body = request.json
        pedido = Pedido.query.get_or_404(id)


        pagamento_confirmado = body.get('pagamento_confirmado')
        data_confirmacao_pagamento = body.get('data_confirmacao_pagamento')
        numero_parcelas = body.get('numero_parcelas')


        if  isinstance(pagamento_confirmado, bool) and isinstance(data_confirmacao_pagamento, str) and isinstance(numero_parcelas, int):

            pedido.pagamento_confirmado = pagamento_confirmado
            pedido.data_confirmacao_pagamento = data_confirmacao_pagamento
            pedido.numero_parcelas = numero_parcelas

            pedido.update()
            return pedido.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        pedido = Pedido.query.get_or_404(id)

        pagamento_confirmado = body.get('pagamento_confirmado', pedido.pagamento_confirmado)
        data_confirmacao_pagamento = body.get('data_confirmacao_pagamento', pedido.data_confirmacao_pagamento)
        numero_parcelas = body.get('numero_parcelas', pedido.numero_parcelas)


        if  isinstance(pagamento_confirmado, bool) and isinstance(data_confirmacao_pagamento, str) and isinstance(numero_parcelas, int):

            pedido.numero_parcelas = numero_parcelas
            pedido.pagamento_confirmado = pagamento_confirmado
            pedido.data_confirmacao_pagamento = data_confirmacao_pagamento

            pedido.update()
            return pedido.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        pedido = Pedido.query.get_or_404(id)
        pedido.delete(pedido)
        return pedido.json()