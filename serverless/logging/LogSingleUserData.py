from Cloud.packages.cloudwatch import logs_manager
from Cloud.packages.constants import constants
from aws_lambda_powertools import Tracer

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    user = event[constants.TABLE_PK]
    # invoke lambda to log individual
    logs_manager.log_user_stats(user)

##############################################################################################
