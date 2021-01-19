from Cloud.packages.dynamo import dynamo_manager, controller
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    user_id = json.loads(event["body"]).pop(constants.TABLE_PK)

    status_code = 200
    message = "Entry on Users table deleted successfully"

    try:
        dynamo_manager.delete_item(constants.USERS_TABLE_NAME,
                                   constants.TABLE_PK,
                                   user_id)
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
