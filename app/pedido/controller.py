from app.pedido.models import Pedido
from flask import request, jsonify
from flask.views import MethodView


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