from Cloud.packages.controller import check_in_controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    body = event.get("body")
    status_code = 200
    output = None

    user_id = ""
    longitude = ""
    latitude = ""

    try:
        output = check_in_controller.check_in_block({"user_id": user_id,
                                                     "longitude": longitude,
                                                     "latitude": latitude})
    except Exception as e:
        status_code = 400
        log.error(e)

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": output,
        }),
    }

##############################################################################################
