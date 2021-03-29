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
    output = []
    status_code = 200

    if body is None:
        return {
            "statusCode": 410,
            "body": json.dumps({
                "message": "Body can't be empty.",
            }),
        }

    user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        stats = logs_manager.get_user_stats(user_id)

        if stats is not None:
            for key, value in stats.items():
                title = key.replace("_", " ").title()
                val = str(value)
                output.append({title: val})

        else:
            output = "No data found for queried User"
            status_code = 502

    except Exception as e:
        log.error(e)
        status_code = 502

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": output,
        }),
    }

##############################################################################################
