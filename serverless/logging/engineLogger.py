from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.constants import constants
from aws_lambda_powertools import Tracer
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the blocks table with the captured blocks from the user.
    This SNS event will be called inside of an Ec2 instance from the search engine
    """

    # Get the records list
    records = event["Records"][0]
    sns_message = records["Sns"]["Message"]
    sns_subject = records["Sns"]["Subject"]

    if sns_message:
        # LOG TO CLOUDWATCH
        logs_manager.create_or_update_log(log_group=constants.SEARCH_ENGINE_LOG_GROUP,
                                          log_stream=sns_subject,
                                          message=sns_message)

        # log.info(f"logging info for {sns_subject}")

##############################################################################################
