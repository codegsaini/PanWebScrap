from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)

cors = CORS(app)
app.config['CORS-HEADERS'] = "Content-Type"

api = Api(app)

class Main(Resource):
    @staticmethod
    def get(self):
        print(request.args.get("name"))

api.add_resource(Main, "/")

if __name__ == "__main__":
    app.run()
