from Cloud.packages.sns import sns_manager
from aws_lambda_powertools import Tracer
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    # send to sns event to delete all items with C# (faster)
    topic_arn = sns_manager.get_topic_by_name("DropBlocksTable")[0]["TopicArn"]
    sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message="delete all blocks", subject="delete all blocks")

##############################################################################################
