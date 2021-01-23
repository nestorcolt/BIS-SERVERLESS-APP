from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def lambda_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the blocks table with the captured blocks from the user.
    This SNS event will be called inside of an Ec2 instance from the search engine
    """

    # Get the records list
    records = event["Records"][0]
    sns_message = json.loads(records["Sns"]["Message"])

    if sns_message:
        user = sns_message["user_id"]
        data = sns_message["data"]
        stream_name = f"User-{user}"

        # LOG TO CLOUDWATCH
        logs_manager.create_or_update_log(log_group=constants.SEARCH_ENGINE_LOG_GROUP,
                                          log_stream=stream_name,
                                          message=data)

        log.info(f"logging info for user: {user}")

##############################################################################################
