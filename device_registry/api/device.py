from flask_restful import Resource
import json
from device_registry.utils import db_connect

class Device(Resource):
    def __init__(self):
        self.client = db_connect()


    def get(self, id):
        data = self.client.from_('device_registry').select('*').eq('id', id).execute()

        response = data.json()

        json_response = json.loads(response)

        if len(json_response['data']) == 0:
            return {'message': 'Device not found'}, 404
        else:
            return {'message': 'Success', 'data': json_response['data']}, 200

    def delete(self, id):
        data = self.client.from_('device_registry').delete().eq('id', id).execute()

        response = data.json() 

        json_response = json.loads(response)

        if len(json_response['data']) == 0:
            return {'message': 'Device not found'}, 404
        else:
            return {'message': 'Device deleted'}, 200