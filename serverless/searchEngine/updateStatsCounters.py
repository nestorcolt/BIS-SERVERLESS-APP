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
    records = event["Records"]

    for record in records:
        event_name = record["eventName"]

        if event_name == "INSERT" or event_name == "MODIFY":
            record_handler(record)


##############################################################################################

def record_handler(record):
    new_image = record["dynamodb"]["NewImage"]
    old_image = record["dynamodb"]["OldImage"]

    print(new_image)
