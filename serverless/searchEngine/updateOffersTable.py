from Cloud.packages.dynamo import controller
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def lambda_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the offer table with data of the seen offer to later send
    this to analytics
    """
    # Get the records list
    offer = json.loads(event["Records"][0]["Sns"]["Message"])

    user = offer["user_id"]
    data = offer["data"]

    # controller.put_new_block(user, data)
    log.info(f"New entry created for user {user} on the blocks table. Data: {data}")

##############################################################################################
