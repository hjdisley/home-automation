from flask import Flask
import markdown
import os
from flask_restful import Resource, Api, reqparse
import json
from device_registry.utils import db_connect



# Create and instance of Flask
app = Flask(__name__)

api = Api(app)

@app.route('/')
def index():

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        
        return markdown.markdown(content)

    
class DeviceList(Resource):
    def __init__(self):
        self.client = db_connect()

    def get(self):
        data = self.client.from_('device_registry').select('*').execute()

        response = data.json()

        json_response = json.loads(response)

        return {'message': 'Success', 'data': json_response['data']}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        args = parser.parse_args()

        data = self.client.from_('device_registry').insert(args).execute()

        return {'message': 'Device registered', 'data': args}, 201

class Device(Resource):
    def __init__(self):
        pass

    def get(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/devices/<string:id>')