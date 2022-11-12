import json

from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidatos_blueprint import candidatos_blueprint
from blueprints.mesas_blueprint import mesas_blueprint
from blueprints.partidos_blueprint import partidos_blueprint
from blueprints.votos_blueprint import votos_blueprint
from blueprints.reporte_blueprint import reports_blueprints


app = Flask(__name__)
CORS(app)
# Register blueprints
app.register_blueprint(candidatos_blueprint)
app.register_blueprint(mesas_blueprint)
app.register_blueprint(partidos_blueprint)
app.register_blueprint(votos_blueprint)
app.register_blueprint(reports_blueprints)

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