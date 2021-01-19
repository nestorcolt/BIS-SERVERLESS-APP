from Cloud.packages.dynamo import controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def function_handler(event, context):
    blocks_response = []
    status_code = 200
    user_id = None
    blocks = []

    body = event["body"]

    if body is not None:
        user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        blocks = controller.get_blocks(user_id)
    except Exception as e:
        log.error(e)
        status_code = 410

    if blocks:
        # cast any Decimal value to float because Decimal is not json serializable
        blocks_response = list(map(lambda block: controller.map_response_body({}, block), blocks))

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": blocks_response,
        }),
    }

##############################################################################################
