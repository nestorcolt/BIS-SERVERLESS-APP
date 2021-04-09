from Cloud.packages.controller import check_in_controller
from Cloud.packages.controller import user_controller
from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from Cloud.packages.sns import sns_manager
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
user_id = "5"
longitude = ""
latitude = ""


def function_handler(event, context):
    # body = event.get("body")
    status_code = 200
    output = None

    check_in_controller.check_in_block({"user_id": user_id, "longitude": longitude, "latitude": latitude})

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": output,
        }),
    }

##############################################################################################
