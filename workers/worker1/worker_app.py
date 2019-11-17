from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

import requests
import subprocess
import json


app = Flask(__name__)
api = Api(app)



class Hello(Resource):
    def get(self):
        
        return {"msg": "Hello worker1"}
api.add_resource(Hello,'/api/v1/task/')


# @app.route('/hello')
# def hello():
#     return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001, threaded=True)