from Cloud.packages.dynamo import dynamo_manager, controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def function_handler(event, context):
    user_id = json.loads(event["body"]).get(constants.TABLE_PK)
    blocks_response = []
    status_code = 200
    blocks = []

    try:
        blocks = controller.get_user_blocks(user_id)
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
