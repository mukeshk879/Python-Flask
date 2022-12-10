from pymongo import MongoClient
from flask import Response
import src.utils.service_constants as constants
from src.utils.log_util import logger
import json


mongodb_url = "mongodb://localhost:27017"
connection = MongoClient(mongodb_url)
db = connection["testdb"]


def read():
    # Response object
    response = Response()
    del response.headers["content-length"]
    response.headers["content-type"] = constants.CONTENT_TYPE
    response_body = {}

    try:
        collection = db["test"]
        data = []
        for row in collection.find():
            row["_id"] = str(row["_id"])
            data.append(row)
        if data:
            response_body["message"] = "Details"
            response_body["data"] = data
            response.body = response_body
            response.status_code = 200
        else:
            response_body["message"] = "Data not found"
            response.body = response_body
            response.status_code = 204

    except Exception as e:
        logger.info(str(e))
        response_body["message"] = str(e)
        response.body = response_body
        response.status_code = 500
    finally:
        # Closing the db connection
        connection.close()

    return response_body


