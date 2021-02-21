from Cloud.packages.requests import request_manager
from Cloud.packages.constants import constants
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

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
    user_id = json.loads(event["Records"][0]["Sns"]["Message"])[constants.TABLE_PK]
    response = request_manager.send_error_to_web(user_id)
    log.info(f"Response of request: {response}")

##############################################################################################
