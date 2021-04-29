from Cloud.packages.controller import user_controller
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import simplejson
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def function_handler(event, context):
    api_response = []
    status_code = 200
    user_data = None
    dynamo_data = None

    body = event["body"]

    if body is not None:
        user_data = json.loads(body)

    try:
        dynamo_data = user_controller.get_user_data(user_data)
        access_token = user_controller.get_access_token(dynamo_data["refresh_token"])
        dynamo_data["access_token"] = access_token
    except Exception as e:
        log.error(e)
        status_code = 410

    if dynamo_data:
        # cast any Decimal value to float because Decimal is not json serializable
        api_response = utils.map_response_body({}, dynamo_data)

    return {
        "statusCode": status_code,
        "body": simplejson.dumps({
            "message": api_response,
        }, use_decimal=True),
    }

##############################################################################################
# this = function_handler({"body": '{"user_id": "7"}'}, "")
# print(this)
