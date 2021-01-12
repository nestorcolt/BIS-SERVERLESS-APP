from Cloud.packages.Ec2 import instance_initializer, ec2_manager
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def start_handler(event, context):
    # Get the records list
    records = event["Records"][0]

    try:
        message = json.loads(records["Sns"]["Message"])
        user_id = message.get("user_id")

        if user_id:
            user_id_value = utils.sns_get_value(user_id)
            # New instance is created with user ID on its name [User-ID]
            instance_initializer.create_instance_handle_from_template(user_id_value,
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
            "message": f"Instance created for user: {user_id_value}",
        }),
    }


##############################################################################################


def terminate_handler(event, context):
    # Get the records list
    records = event["Records"][0]

    try:
        message = json.loads(records["Sns"]["Message"])
        user_id = message.get("user_id")

        if user_id:
            user_id_value = utils.sns_get_value(user_id)
            instance_name = f"User-{user_id_value}"

            # Ec2 instance delete
            ec2_manager.delete_instance_handle(instance_name)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        log.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Instance deleted for user: {user_id_value}",
        }),
    }


##############################################################################################


def modify_state_handler(event, context):
    # Get the records list
    records = event["Records"][0]

    try:
        message = json.loads(records["Sns"]["Message"])
        state = message.get("search_blocks")
        user_id = message.get("user_id")

        if user_id and state:
            user_search_state_value = utils.sns_get_value(state)
            user_id_value = utils.sns_get_value(user_id)
            instance_name = f"User-{user_id_value}"

            if user_search_state_value is True:
                ec2_manager.start_instance_handle(instance_name)
            else:
                ec2_manager.stop_instance_handle(instance_name)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        log.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Instance state modified for user: {user_id_value}",
        }),
    }
