from Cloud.packages.dynamo import dynamo_manager, controller
from Cloud.packages.constants import constants
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    new_headers = controller.map_request_body({}, event)

    try:
        dynamo_manager.create_item(constants.USERS_TABLE_NAME, dictionary_item=new_headers)
    except Exception as e:
        log.error(e)
        return {"success": False, "message": e, "data": {}}

    return {"success": True, "message": "Entry created", "data": new_headers}

##############################################################################################
