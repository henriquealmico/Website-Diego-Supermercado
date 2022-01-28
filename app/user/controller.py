from click import decorators
from app.user.models import User
from flask import render_template, request, jsonify
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail, jwt
from flask_jwt_extended import create_access_token, jwt_required
import bcrypt


class UserG(MethodView): #/user

    def post(self):

        body = request.json

        idade = body.get('idade')
        cpf = body.get('cpf')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        endereco = body.get('endereco')
        cidade = body.get('cidade')
        estado = body.get('estado')
        cep = body.get('cep')
        ja_realizou_compra = body.get('ja_realizou_compra')
        como_descobriu_site = body.get('como_descobriu_site')


        if  isinstance(idade, int) and isinstance(cpf, str) and isinstance(cpf, str) and\
            isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str) and\
            isinstance(endereco, str) and isinstance(cidade, str) and isinstance(estado, str) and\
            isinstance(cep, str) and isinstance(ja_realizou_compra, bool) and isinstance(como_descobriu_site, str):

            user = User.query.filter_by(email=email).first()

            if user:
                return {"code_status":"user already exists"}, 409 

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            user = User(idade=idade, cpf=cpf, nome=nome, email=email, senha = senha_hash,\
                        endereco=endereco, cidade=cidade, estado=estado, cep=cep,\
                        ja_realizou_compra=ja_realizou_compra, como_descobriu_site=como_descobriu_site)

            user.save()

            mensagem = Message(
                sender = "henriquealmico@poli.ufrj.br",
                recipients = [email],
                subject= "Bem vindo ao supermercado digital!",
                html = render_template('email-boas-vindas.html', nome = nome)
            )

            mail.send(mensagem)

            return user.json(), 201

        else:
            return {"code_status":"invalid data in request"}, 400


    def get(self):

        users = User.query.all()
        return jsonify([user.json() for user in users]), 200


class UserId(MethodView): #/user/<int:id>

    decorators = [jwt_required()]

    def get(self, id):

        user = User.query.get_or_404(id)
        return user.json()

    def put(self, id):

        body = request.json
        user = User.query.get_or_404(id)

        idade = body.get('idade')
        cpf = body.get('cpf')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        endereco = body.get('endereco')
        cidade = body.get('cidade')
        estado = body.get('estado')
        cep = body.get('cep')
        ja_realizou_compra = body.get('ja_realizou_compra')
        como_descobriu_site = body.get('como_descobriu_site')


        if  isinstance(idade, int) and isinstance(cpf, str) and isinstance(cpf, str) and\
            isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str) and\
            isinstance(endereco, str) and isinstance(cidade, str) and isinstance(estado, str) and\
            isinstance(cep, str) and isinstance(ja_realizou_compra, bool) and isinstance(como_descobriu_site, str):

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            user.idade = idade
            user.cpf = cpf
            user.nome = nome
            user.email = email
            user.senha = senha_hash
            user.endereco = endereco
            user.cidade = cidade
            user.estado = estado
            user.cep = cep
            user.ja_realizou_compra = ja_realizou_compra
            user.como_descobriu_site = como_descobriu_site

            user.update()
            return user.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def patch(self, id):

        body = request.json
        user = User.query.get_or_404(id)

        idade = body.get('idade', user.idade)
        cpf = body.get('cpf', user.cpf)
        nome = body.get('nome', user.nome)
        email = body.get('email', user.email)
        senha = body.get('senha', user.senha)
        endereco = body.get('endereco', user.endereco)
        cidade = body.get('cidade', user.cidade)
        estado = body.get('estado', user.estado)
        cep = body.get('cep', user.cep)
        ja_realizou_compra = body.get('ja_realizou_compra', user.ja_realizou_compra)
        como_descobriu_site = body.get('como_descobriu_site', user.como_descobriu_site)


        if  isinstance(idade, int) and isinstance(cpf, str) and isinstance(cpf, str) and\
            isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str) and\
            isinstance(endereco, str) and isinstance(cidade, str) and isinstance(estado, str) and\
            isinstance(cep, str) and isinstance(ja_realizou_compra, bool) and isinstance(como_descobriu_site, str):

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            user.idade = idade
            user.cpf = cpf
            user.nome = nome
            user.email = email
            user.senha = senha_hash
            user.endereco = endereco
            user.cidade = cidade
            user.estado = estado
            user.cep = cep
            user.ja_realizou_compra = ja_realizou_compra
            user.como_descobriu_site = como_descobriu_site

            user.update()
            return user.json(), 200
        
        else:

            return {"code_status":"invalid data in request"}, 400


    def delete(self, id):

        user = User.query.get_or_404(id)
        user.delete(user)
        return user.json()
        
            

class UserLogin(MethodView): #/login

    def post(self):

        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.hashpw(senha.encode(), bcrypt.gensalt()):
            return {"Error":"Usuário ou senha inválidos"}

        token = create_access_token(identity = user.id)

        return {"token": token}, 200

            
