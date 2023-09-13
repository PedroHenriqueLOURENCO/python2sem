from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class main(Resource):
    def get(self):
        return "Funciona"
    def post(self):
        ...
    def put(self):
        ...
    def delete(self):
        ...

class version(Resource):
    def get(self):
        return "0.0.1"
    def post(self):
        ...
    def put(self):
        ...
    def delete(self):
        ...

api.add_resource(main, "/")
api.add_resource(version, "/version")

if __name__ == "__main__":
    app.run(port=8080)