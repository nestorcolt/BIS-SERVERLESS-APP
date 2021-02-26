from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from aws_lambda_powertools import Tracer
import boto3
import json

##############################################################################################
client = boto3.client('lambda')

tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    # LOG TO CLOUDWATCH ALL USERS WITH STATUS SEARCHING
    last_active = controller.get_last_active_users()

    for user_data in last_active["Items"]:
        user = user_data[constants.TABLE_PK]

        # invoke lambda to log individual
        client.invoke(
            FunctionName='LogSingleUserData',
            InvocationType='Event',
            Payload=json.dumps({constants.TABLE_PK: user})
        )

##############################################################################################
