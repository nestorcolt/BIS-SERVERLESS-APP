from Cloud.packages.controller import check_in_controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    """
    Check in function, this will handle the api call for the amazon flex check in operation
    :param event: AWS related
    :param context: AWS related
    :return: api response
    """
    body = json.loads(event["body"])

    user_id = body.get("user_id")
    longitude = body.get("longitude")
    latitude = body.get("latitude")

    try:
        output = check_in_controller.check_in_block({"user_id": user_id,
                                                     "longitude": longitude,
                                                     "latitude": latitude})
        response = output["response"]
        message = output["message"]

        status_code = response.status_code

        if status_code == 200:
            message = message + "Logout and login again in your Amazon Flex app to see the changes"

    except Exception as e:
        status_code = 400
        message = "Something went wrong with the check-in operation"
        log.error(e)

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
        }),
    }

##############################################################################################
