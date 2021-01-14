from Cloud.packages.constants import constants
from Cloud.packages.sns import sns_manager
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def lambda_handler(event, context):
    """
    The main handler for process the records coming from dynamo stream events. This divide in 3 the event type
    and publish the record message to the respective SNS topic for the search engine server state processing.

    Start Server
    Pause Server
    Stop Server

    Are the states handled by SNS topics to trigger the lambdas in charge of those instance operations.

    :param event: Records from Dynamo
    :param context: Lambda context AWS
    :return:
    """
    # Get the records list
    records = event["Records"]

    try:
        for record in records:
            process_record(record)

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

def process_record(record):
    """
    Process the record on the handler iteration
    :param record: dictionary - Record inner dictionary
    :return:
    """
    event_name = record["eventName"]
    record_info = record["dynamodb"]

    if event_name == "INSERT":
        image_data = record_info.get("NewImage")
        log.debug(f"CreateEvent: {image_data}")
        user_id_value = utils.sns_get_value(image_data["user_id"])
        topic_arn = sns_manager.get_topic_by_name(constants.START_SE_SNS_NAME)[0]["TopicArn"]
        sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message=json.dumps(user_id_value), subject="DynamoStream")

    elif event_name == "REMOVE":
        image_data = record_info.get("Keys")
        log.debug(f"DeleteEvent: {image_data}")
        user_id_value = utils.sns_get_value(image_data["user_id"])
        topic_arn = sns_manager.get_topic_by_name(constants.STOP_SE_SNS_NAME)[0]["TopicArn"]
        sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message=json.dumps(user_id_value), subject="DynamoStream")

    elif event_name == "MODIFY":
        image_data = record_info.get("NewImage")
        log.debug(f"ModifyEvent: {image_data}")
        user_id_value = utils.sns_get_value(image_data["user_id"])
        topic_arn = sns_manager.get_topic_by_name(constants.STOP_SE_SNS_NAME)[0]["TopicArn"]
        sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message=json.dumps(user_id_value), subject="DynamoStream")
