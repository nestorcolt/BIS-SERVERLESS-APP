from Cloud.packages.dynamo import dynamo_manager, controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    new_headers = controller.map_request_body({}, json.loads(event["body"]))
    status_code = 200
    message = "Entry on Users table created successfully"

    # Dirty fix to add the access_token property to the users table always
    new_headers["access_token"] = ""

    try:
        dynamo_manager.create_item(constants.USERS_TABLE_NAME, dictionary_item=new_headers)
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
