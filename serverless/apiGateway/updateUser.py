from Cloud.packages.dynamo import dynamo_manager, controller
from Cloud.packages.constants import constants
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    new_headers = controller.map_request_body({}, event)
    user_id = new_headers.pop(constants.TABLE_PK)

    try:
        dynamo_manager.update_item(constants.USERS_TABLE_NAME,
                                   constants.TABLE_PK,
                                   user_id,
                                   new_headers)
    except Exception as e:
        log.error(e)
        return {"success": False, "message": e, "data": {}}

    return {"success": True, "message": "Entry created", "data": new_headers}

##############################################################################################
