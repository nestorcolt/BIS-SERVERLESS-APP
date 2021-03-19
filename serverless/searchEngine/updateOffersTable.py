from Cloud.packages.dynamo import controller
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the offer table with data of the seen offer to later send
    this to analytics
    """
    # Get the records list
    offer = json.loads(event["Records"][0]["Sns"]["Message"])

    validated = offer["validated"]
    user = offer["user_id"]
    data = offer["data"]

    controller.put_new_offer(user, validated, data)

##############################################################################################
