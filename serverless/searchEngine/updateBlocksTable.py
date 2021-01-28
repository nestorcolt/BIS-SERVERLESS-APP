from Cloud.packages.dynamo import controller
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def function_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the blocks table with the captured blocks from the user.
    This SNS event will be called inside of an Ec2 instance from the search engine
    """
    # Get the records list
    block = json.loads(event["Records"][0]["Sns"]["Message"])

    user = block["user_id"]
    data = block["data"]

    controller.put_new_block(user, data)
    log.info(f"New entry created for user {user} on the blocks table. Data: {data}")

##############################################################################################
