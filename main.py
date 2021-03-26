from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

yourJson = [
    {
        "id": 0,
        "content": "You can put whatever you want in key value pairs here",
    }
]


class APIExample(Resource):
    def get(self):
        return yourJson


api.add_resource(APIExample, "/api-example", "/api-example/")

if __name__ == '__main__':
    app.run(debug=True)