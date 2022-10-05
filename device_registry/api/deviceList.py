from flask_restful import Resource, reqparse
from device_registry.utils import db_connect
import json


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