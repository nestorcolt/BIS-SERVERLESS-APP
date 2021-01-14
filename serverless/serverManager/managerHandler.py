from Cloud.packages.Ec2 import instance_initializer, ec2_manager
from Cloud.packages.constants import constants
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def start_handler(event, context):
    # Get the records list
    records = event["Records"][0]
    user_id = json.loads(records["Sns"]["Message"])

    try:
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
            "message": f"Instance created for user: {user_id}",
        }),
    }


##############################################################################################


def terminate_handler(event, context):
    # Get the records list
    records = event["Records"][0]
    user_id = json.loads(records["Sns"]["Message"])

    try:
        if user_id:
            instance_name = f"User-{user_id}"

            # Ec2 instance delete
            ec2_manager.delete_instance_handle(instance_name)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        log.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Instance deleted for user: {user_id}",
        }),
    }

##############################################################################################
