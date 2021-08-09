from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.constants import constants
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    status_code = 200
    user_id = None
    logs = []

    body = event["body"]

    if body is not None:
        user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        logs = logs_manager.describe_search_engine_logs(user_id)
    except Exception as e:
        log.error(e)
        status_code = 410

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": logs,
        }),
    }

##############################################################################################
