from Cloud.packages.dynamo import dynamo_manager
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################

tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    new_headers = utils.map_request_body({}, json.loads(event["body"]))
    status_code = 200
    message = "Entry on Users table created successfully"

    # Dirty fix to add the access_token property to the users table always
    new_headers["access_token"] = ""

    try:
        response = dynamo_manager.create_item(constants.USERS_TABLE_NAME, dictionary_item=new_headers)
    except Exception as e:
        log.error(e)
        message = e
        status_code = 410

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
        }),
    }

##############################################################################################
