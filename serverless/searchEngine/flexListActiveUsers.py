from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from Cloud.packages.sns import sns_manager
import simplejson


##############################################################################################

def function_handler(event, context):
    """
    Checks for an attribute name "last_active" and if the time span is greater than 30 minutes ago from now
    will start the instance with the user ID
    :return:
    """
    last_active = controller.get_last_active_users()

    for user_data in last_active["Items"]:
        search_blocks = user_data.get("search_blocks", False)
        access_token = user_data.get("access_token", "")

        if not search_blocks:
            continue

        if len(access_token) == 0:
            topic_arn = sns_manager.get_topic_by_name(constants.AUTHENTICATE_SE_SNS_NAME)[0]["TopicArn"]
            sns_manager.sns_publish_to_topic(topic_arn=topic_arn,
                                             message=simplejson.dumps(user_data, use_decimal=True),
                                             subject="Get access token for user")
            continue

        # If passed all validations let user search
        topic_arn = sns_manager.get_topic_by_name(constants.START_SE_SNS_NAME)[0]["TopicArn"]
        sns_manager.sns_publish_to_topic(topic_arn=topic_arn,
                                         message=simplejson.dumps(user_data, use_decimal=True),
                                         subject="User filters for search engine")

##############################################################################################
