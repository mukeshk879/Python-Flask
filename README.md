# Python-Flask


import logging
from flask import Flask, jsonify, request, json
import configparser
import requests



app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read("service/config_dev.ini")



@app.route("/test1", methods=["POST"])
def test1():

    url = "http://localhost:5000/test2"
    payload = '{"name": "Mukesh2", "id": 2}'
    res = requests.post(url,
                        data=payload,
                        headers={'SM_USER': 'Mukesh'})
    data = json.loads(res.content)
    return jsonify(data)
    
    
if __name__ == '__main__':
    app.run(debug=True)






