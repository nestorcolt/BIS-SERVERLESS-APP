from Cloud.packages.s3 import controller as s3_controller
from Cloud.packages.constants import constants as cns
from Cloud.packages.sqs import sqs_manager
from Cloud.packages import logger
import boto3
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
    records = event["Records"]
    offer_dictionary = s3_controller.read_object(cns.OFFERS_BUCKET_NAME, cns.OFFERS_BUCKET_KEY) or "{}"
    offer_dictionary = json.loads(offer_dictionary)

    for record in records:
        body = json.loads(record["body"])
        for offer in body:
            validated = offer["validated"]
            user = offer["user_id"]
            data = offer["data"]
            offer_dictionary = s3_controller.put_new_offer(offer_dictionary, user, validated, data)

    # creates the new entry on dynamo block table
    s3_controller.put_object(cns.OFFERS_BUCKET_NAME,
                             cns.OFFERS_BUCKET_KEY,
                             json.dumps(offer_dictionary, indent=4, separators=[",", ":"]))

##############################################################################################
