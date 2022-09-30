from flask import Flask, request, jsonify
import requests
import logging

from service import test_service

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/flask/test', methods=['POST'])
def test():
    req_data = request.get_json(force=False)
    logging.info("Payload:\n"+str(req_data)+"\n")

    # return jsonify({"id": "12", "name": "Mukesh Kumar"})
    return jsonify(test_service())


if __name__ == "__main__":
    app.run(debug=True)



