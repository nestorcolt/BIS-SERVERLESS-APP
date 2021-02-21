from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.dynamo import dynamo_manager
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
    # Get the records list
    user_id = json.loads(event["Records"][0]["Sns"]["Message"])[constants.TABLE_PK]
    user_stream = constants.USER_PLACEHOLDER.format(user_id)

    if user_id:
        # update dynamo DB
        dynamo_manager.update_item(constants.USERS_TABLE_NAME,
                                   constants.TABLE_PK,
                                   str(user_id),
                                   {"search_blocks": False})

        message = "WARNING: User has been stopped due lack of schedule data"
        logs_manager.create_or_update_log(constants.SEARCH_ENGINE_LOG_GROUP, user_stream, message)

##############################################################################################
