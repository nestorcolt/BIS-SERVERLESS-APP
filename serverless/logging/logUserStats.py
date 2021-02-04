from Cloud.packages.cloudwatch import logs_manager
from aws_lambda_powertools import Tracer

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    # LOG TO CLOUDWATCH ALL USERS WITH STATUS SEARCHING
    logs_manager.log_all_users()

##############################################################################################
