from datetime import datetime
from app.cupons.models import Cupom
from flask import request, jsonify
from flask.views import MethodView



class CupomG(MethodView): #/cupom

    def post(self):

        body = request.json

        desconto = body.get('desconto')
        data_inicio = body.get('data_inicio')
        código = body.get('código')
        forma_utilizacao = body.get('forma_utilizacao')
        campanha = body.get('campanha')
        limite_usuarios = body.get('limite_usuarios')
        objetivo = body.get('objetivo')
        data_termino = body.get('data_termino')


        if  isinstance(desconto, str) and isinstance(data_inicio, datetime) and isinstance(código, str) and\
            isinstance(forma_utilizacao, str) and isinstance(campanha, str) and isinstance(limite_usuarios, int) and\
            isinstance(objetivo, str) and isinstance(data_termino, datetime):

            cupom = Cupom.query.filter_by(código=código).first()

            if cupom:
                return {"code_status":"cupom already exists"}, 400

            cupom = Cupom(desconto=desconto, data_inicio=data_inicio, código=código, forma_utilizacao=forma_utilizacao,\
                                campanha=campanha, limite_usuarios=limite_usuarios, objetivo=objetivo,\
                                data_termino=data_termino)

            cupom.save()
            return cupom.json(), 201
        
        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        cupons = Cupom.query.all()
        return jsonify([cupom.json() for cupom in cupons]), 200


class CupomId(MethodView): #/cupom/<int:id>

    def get(self, id):

        cupom = Cupom.query.get_or_404(id)
        return cupom.json()

    def put(self, id):

        body = request.json
        cupom = Cupom.query.get_or_404(id)

        desconto = body.get('desconto')
        data_inicio = body.get('data_inicio')
        código = body.get('código')
        forma_utilizacao = body.get('forma_utilizacao')
        campanha = body.get('campanha')
        limite_usuarios = body.get('limite_usuarios')
        objetivo = body.get('objetivo')
        data_termino = body.get('data_termino')


        if  isinstance(desconto, float) and isinstance(data_inicio, datetime) and isinstance(código, str) and\
            isinstance(forma_utilizacao, str) and isinstance(campanha, str) and isinstance(limite_usuarios, int) and\
            isinstance(objetivo, str) and isinstance(data_termino, datetime):

            cupom.desconto = desconto
            cupom.data_inicio = data_inicio
            cupom.código = código
            cupom.forma_utilizacao = forma_utilizacao
            cupom.campanha = campanha
            cupom.limite_usuarios = limite_usuarios
            cupom.objetivo = objetivo
            cupom.data_termino = data_termino


            cupom.update()
            return cupom.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        cupom = Cupom.query.get_or_404(id)

        desconto = body.get('desconto', cupom.desconto)
        data_inicio = body.get('data_inicio', cupom.data_inicio)
        código = body.get('código', cupom.código)
        forma_utilizacao = body.get('forma_utilizacao', cupom.forma_utilizacao)
        campanha = body.get('campanha', cupom.campanha)
        limite_usuarios = body.get('limite_usuarios', cupom.limite_usuarios)
        objetivo = body.get('objetivo', cupom.objetivo)
        data_termino = body.get('data_termino', cupom.data_termino)


        if  isinstance(desconto, float) and isinstance(data_inicio, datetime) and isinstance(código, str) and\
            isinstance(forma_utilizacao, str) and isinstance(campanha, str) and isinstance(limite_usuarios, int) and\
            isinstance(objetivo, str) and isinstance(data_termino, datetime):

            cupom.desconto = desconto
            cupom.data_inicio = data_inicio
            cupom.código = código
            cupom.forma_utilizacao = forma_utilizacao
            cupom.campanha = campanha
            cupom.limite_usuarios = limite_usuarios
            cupom.objetivo = objetivo
            cupom.data_termino = data_termino

            cupom.update()
            return cupom.json(), 201
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        cupom = Cupom.query.get_or_404(id)
        cupom.delete(cupom)
        return cupom.json()
