import json

from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    response = {"message": "Welcome to the API"}
    return jsonify(response)

def load_config():
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
    return data


if __name__ == '__main__':
    data_config = load_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))