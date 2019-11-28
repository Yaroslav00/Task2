from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

import requests
import subprocess
import json


app = Flask(__name__)
api = Api(app)



class Hello(Resource):
    def get(self):
       
        return 0



class GetFinishedTasks(Resource):
    def get():
        return 0

class GetProcessingTasks(Resource):
    def get():
        return 0

class GetWaitingTasks(Resource):
    def get():
        return 0

class CreateNewTask(Resource):
    def post():
        return 0
        

class Login(Resource):
    def post():
        print(request.form)
        return request.form



class Signup(Resource):
    def post():
        print(request.form)
        return request.form



api.add_resource(GetProcessingTasks, '/api/v1/get_processing_tasks/')
api.add_resource(GetWaitingTasks, '/api/v1/get_wating_tasks/')
api.add_resource(GetFinishedTasks, '/api/v1/get_finished_tasks/')
api.add_resource(CreateNewTask, '/api/v1/create_new_task/')
api.add_resource(Login, '/api/v1/login/')
api.add_resource(Signup, 'api/v1/signup/')
api.add_resource(Hello,'/api/v1/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)