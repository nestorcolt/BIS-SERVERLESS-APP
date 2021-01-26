from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from Cloud.packages.sns import sns_manager
from Cloud.packages.Ec2 import ec2_manager
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def sleep_status_check_handler(event, context):
    """
    Checks for an attribute name "last_active" and if the time span is greater than 30 minutes ago from now
    will start the instance with the user ID
    :return:
    """
    last_active = controller.get_last_active_users()

    for user in last_active["Items"]:
        search_blocks = user.get("search_blocks", False)

        if search_blocks:
            #  TODO  create topic for set user active for search
            pass
            # topic_arn = sns_manager.get_topic_by_name(constants.START_SE_SNS_NAME)[0]["TopicArn"]
            # sns_manager.sns_publish_to_topic(topic_arn=topic_arn,
            #                                  message=json.dumps(user_id),
            #                                  subject="SleepCheckEvent")

##############################################################################################
