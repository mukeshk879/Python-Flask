from flask import Flask, jsonify, Response, request
import logging
from src.apis.crud_app import blueprint


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
# Blueprint
app.register_blueprint(blueprint, url_prefix="/v1")


@app.route("/", methods=["GET"])
def start():
    response = "Application running..."
    return response


@app.route("/v1/health", methods=["GET"])
def health():
    response = "Application running..."
    return response


if __name__ == "__main__":
    app.run(debug=True)



