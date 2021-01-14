from Cloud.packages.Ec2 import instance_initializer, ec2_manager
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def sleep_handler(event, context):
    # Get the records list
    records = event["Records"][0]

    message = json.loads(records["Sns"]["Message"])
    user_id = message.get("user_id")


##############################################################################################


def wakeup_handler(event, context):
    # Get the records list
    records = event["Records"][0]

    message = json.loads(records["Sns"]["Message"])
    user_id = message.get("user_id")
