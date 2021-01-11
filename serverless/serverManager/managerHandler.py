from Cloud.packages.Ec2 import instance_initializer
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import importlib
import json

importlib.reload(instance_initializer)
importlib.reload(constants)
importlib.reload(utils)

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def lambda_handler(event, context):
    # Get the records list
    records = event["Records"]

    try:
        message = records["Message"]
        user_id = utils.sns_get_value(message["userId"])

        if user_id:
            # New instance is created with user ID on its name [User-ID]
            instance_initializer.create_instance_handle_from_template(user_id,
                                                                      constants.WORKER_LAUNCH_TEMPLATE_NAME,
                                                                      constants.WORKER_SECURITY_GROUP_NAME,
                                                                      constants.SUBNET_NAME)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        log.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "InfoProcessed",
        }),
    }

##############################################################################################
