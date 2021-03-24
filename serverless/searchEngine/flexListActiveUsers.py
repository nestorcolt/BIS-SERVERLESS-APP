from Cloud.packages.dynamo import system_settings_controller
from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from Cloud.packages.utilities import utils
from Cloud.packages.sns import sns_manager
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import simplejson

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    """
    Checks for an attribute name "last_active" and if the time span is greater than 30 minutes ago from now
    will start the instance with the user ID
    :return:
    """

    # set system settings
    settings = system_settings_controller.get_item(version=1)

    if not settings["search_engine"]:
        return

    last_active = controller.get_last_active_users()
    wait_search_value = int(settings.get("search_timeout", 60))  # in seconds

    for user_data in last_active["Items"]:
        search_blocks = user_data.get("search_blocks")
        last_iteration = user_data.get("last_iteration", 0)

        if not search_blocks:
            continue

        # calculates the difference between the current time and the registered time from user item
        last_iteration_difference = abs(min(0, float(last_iteration) - utils.get_unix_time()))

        if last_iteration_difference > wait_search_value:
            # If passed all validations let user search
            topic_arn = sns_manager.get_topic_by_name(constants.SE_START_TOPIC)[0]["TopicArn"]
            sns_manager.sns_publish_to_topic(topic_arn=topic_arn,
                                             message=simplejson.dumps(user_data, use_decimal=True),
                                             subject="User filters for search engine")

##############################################################################################
