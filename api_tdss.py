from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

lista = ["Lucas"]


class Listar(Resource):
    def get(self):
        for elemento in lista:
            dados = elemento + "\n"
        return str(dados)

class Main (Resource):
    def post(self, nome):
        lista.append(str(nome).title())
        return f'Usuario {nome} foi adicionado com sucesso!'
    def put(self):
        ...
    def delete(self, nome):
        if nome in lista:
            for index in range(o, len(lista)):
                if lista[index] == nome:
                    del lista[index]
                    return "elemento removido"
        else:
            return "elemento não existe"
                    

class version(Resource):
    def get(self):
        return "0.0.1"
    def post(self):
        ...
    def put(self):
        ...
    def delete(self):
        ...
api.add_resource(Listar, "/>")
api.add_resource(Main, "/<nome>")
api.add_resource(version, "/version")

if __name__ == "__main__":
    app.run(port=8080)