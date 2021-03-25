from Cloud.packages.dynamo import controller
from aws_lambda_powertools import Tracer
from Cloud.packages import logger

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
    old_image = record["dynamodb"].get("OldImage", None)

    if old_image is None:
        user_id = record["dynamodb"]["Keys"]["user_id"]["S"]
        new_image = record["dynamodb"].get("NewImage")

        # If validated is not present is because this stream comes from the Blocks table
        validated = new_image.get("validated", None)

        if validated is None:
            controller.update_user_stats(user_id=user_id, accepted=1)  # + 1 offer append to the existing counter
            return
        else:
            validated_value = validated["BOOL"]
            # raise counter, if there is no old image that means the record is new
            controller.update_user_stats(user_id, validated=int(validated_value), offer=1)
            return

##############################################################################################
