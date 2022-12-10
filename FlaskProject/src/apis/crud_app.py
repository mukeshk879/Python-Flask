from flask import jsonify, Blueprint
from src.service.crud_service import read
from src.utils.log_util import logger

# Blueprint
blueprint = Blueprint("blueprint", __name__)


@blueprint.route("", methods=["GET"])
def crud_read():
    logger.info("Request received for endpoint:/v1")
    response = read()
    logger.info("Request completed for endpoint:/v1")
    return response


