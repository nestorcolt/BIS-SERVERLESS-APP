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
s = {
    "user_id": "2",
    "refresh_token": "",
    "areas": [],
    "search_blocks": 1,
    "last_active": 0,
    "speed": 1,
    "minimum_price": 20.00,
    "search_schedule": [
        {
            "dayOfWeek": 0,
            "enable": 1,
            "times": [
                {
                    "blockTime": 1,
                    "start": "08:00",
                    "end": "10:00"
                },
                {
                    "blockTime": 1,
                    "start": "08:00",
                    "end": "10:00"
                },
                {
                    "blockTime": 2,
                    "start": "08:00",
                    "end": "10:00"
                },
                {
                    "blockTime": 2,
                    "start": "08:00",
                    "end": "10:00"
                }
            ]
        }
    ]
}
