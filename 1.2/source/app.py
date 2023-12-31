from flask import Flask, request
from flask_restful import Resource, Api

import json
import os

app = Flask(__name__)
api = Api(app)

# Get path to storage data file
storage_path = os.path.realpath('storage.data')

# Create file if not exists
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f)


# Class for working with storage
class KeyValueStorage(Resource):
    # Get and write data
    def get(self):
        key = request.args.get('key')
        if key is not None:
            with open(storage_path, 'r') as f:
                data = json.load(f)
                value = data.get(key, None)
                if value is not None:
                    return {key: value}, 200
                else:
                    return "Key not found", 404
        else:
            all_data = {}
            with open(storage_path, 'r') as f:
                all_data = json.load(f)
            return all_data, 200

    def post(self):
        data = request.get_json()  # Get data from JSON request
        if data is not None and 'key' in data and 'value' in data:
            key = data['key']
            value = data['value']
            with open(storage_path, 'r') as f:
                storage_data = json.load(f)
            storage_data[key] = value
            with open(storage_path, 'w') as f:
                json.dump(storage_data, f)
            return "Data added/updated successfully", 201
        else:
            return "Key and value must be provided in JSON body", 400


# Add route "/"
@app.route('/')
def index():
    return """Welcome to the Key-Value Storage API. You can use the following routes:

- GET /api/v1/storage/json to get all data
- GET /api/v1/storage/json?key=key to get data by key
- POST /api/v1/storage/json to add or update data (provide JSON body with 'key' and 'value')
"""


# Add API routes
api.add_resource(KeyValueStorage, '/api/v1/storage/json', '/api/v1/storage/json/all', '/api/v1/storage/json/write',
                 '/api/v1/storage/json/read')

if __name__ == '__main__':
    app.run(debug=True)
