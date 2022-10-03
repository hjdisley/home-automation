from flask import Flask
import markdown
import os
from flask_restful import Resource, Api


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
    def get(self):
        return {'devices': 'HELLO WORLD'}

api.add_resource(DeviceList, '/devices')