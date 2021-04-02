from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from Cloud.packages.sns import sns_manager
from aws_lambda_powertools import Tracer
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    body = event.get("body")
    message = "Success"
    status_code = 200

    if body is None:
        # send to sns event to delete all items with C# (faster)
        topic_arn = sns_manager.get_topic_by_name("DropBlocksTable")[0]["TopicArn"]
        sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message="delete all blocks", subject="delete all blocks")
        return {
            "statusCode": status_code,
            "body": json.dumps({
                "message": message,
            }),
        }

    user_id = json.loads(body).get(constants.TABLE_PK)

    try:
        blocks = controller.get_blocks(user_id)

        if blocks:
            # cast any Decimal value to float because Decimal is not json serializable
            controller.delete_blocks(blocks)

    except Exception as e:
        status_code = 501
        log.error(e)
        message = e

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
        }),
    }

##############################################################################################
