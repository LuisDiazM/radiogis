from flask import Flask
from flask_restful import Api
from app.controllers import HelloWorld


app = Flask(__name__)
api = Api(app=app, prefix="/api/v1")

api.add_resource(HelloWorld, '/')
