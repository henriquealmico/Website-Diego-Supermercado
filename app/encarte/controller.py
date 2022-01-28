from app.encarte.models import Encarte
from flask import request, jsonify
from flask.views import MethodView


class EncarteG(MethodView): #/encarte

    def post(self):

        body = request.json


        data_inicio = body.get('data_inicio')
        data_termino = body.get('data_termino')
        nome = body.get('nome')


        if  isinstance(data_inicio, str) and isinstance(data_termino, str) and isinstance(nome, str):

            encarte = Encarte(nome=nome, data_inicio=data_inicio, data_termino=data_termino)

            encarte.save()
            return encarte.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        encartes = Encarte.query.all()
        return jsonify([encarte.json() for encarte in encartes]), 200


class EncarteId(MethodView): #/encarte/<int:id>

    def get(self, id):

        encarte = Encarte.query.get_or_404(id)
        return encarte.json()

    def put(self, id):

        body = request.json
        encarte = Encarte.query.get_or_404(id)


        data_inicio = body.get('data_inicio')
        data_termino = body.get('data_termino')
        nome = body.get('nome')


        if  isinstance(data_inicio, str) and isinstance(data_termino, str) and isinstance(nome, str):

            encarte.data_inicio = data_inicio
            encarte.data_termino = data_termino
            encarte.nome = nome

            encarte.update()
            return encarte.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        encarte = Encarte.query.get_or_404(id)

        data_inicio = body.get('data_inicio', encarte.data_inicio)
        data_termino = body.get('data_termino', encarte.data_termino)
        nome = body.get('nome', encarte.nome)


        if  isinstance(data_inicio, str) and isinstance(data_termino, str) and isinstance(nome, str):

            encarte.nome = nome
            encarte.data_inicio = data_inicio
            encarte.data_termino = data_termino

            encarte.update()
            return encarte.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        encarte = Encarte.query.get_or_404(id)
        encarte.delete(encarte)
        return encarte.json()