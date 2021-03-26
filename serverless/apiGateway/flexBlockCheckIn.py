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

    return "OK"

##############################################################################################
