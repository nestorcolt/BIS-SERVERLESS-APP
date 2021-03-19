from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
# from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################
# tracer = Tracer()


# @tracer.capture_lambda_handler
def function_handler(event, context):
    body = event.get("body")

    if body is None:
        # send to sns event to delete all items with C# (faster)
        return "OK"

    user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        blocks = controller.get_blocks(user_id)

        if blocks:
            # cast any Decimal value to float because Decimal is not json serializable
            controller.delete_blocks(blocks)

    except Exception as e:
        log.error(e)

    return "OK"

##############################################################################################
