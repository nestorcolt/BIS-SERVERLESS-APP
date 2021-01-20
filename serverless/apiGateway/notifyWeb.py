from Cloud.packages.dynamo import controller
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
    blocks = json.loads(records["Sns"]["Message"])["blocks"]

    for block in blocks:
        user = block["user_id"]
        data = block["data"]
        response = controller.send_block_to_web(user, data)
        log.info(f"Response of request: {response.status_code}")

##############################################################################################
