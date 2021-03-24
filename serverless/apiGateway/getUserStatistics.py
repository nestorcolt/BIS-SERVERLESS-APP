from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.constants import constants
from collections import OrderedDict
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################


def function_handler(event, context):
    body = event.get("body")

    if body is None:
        return "Request Failed. body can't be empty"

    user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        stats = logs_manager.get_user_stats(user_id)

        if stats is None:
            return {"status_code": "failed", "payload": {"Status": "No data found for queried User"}}

        output = OrderedDict(dict())

        for key, value in stats.items():
            title = key.replace("_", " ").title()
            val = str(value)
            output[title] = val

    except Exception as e:
        log.error(e)
        return {"status_code": "failed", "payload": {"Status": "Server Error"}}

    return {"status_code": "success", "payload": output}

##############################################################################################
