from Cloud.packages.dynamo import dynamo_manager
from decimal import Decimal
import boto3
import json


##############################################################################################

def function_handler(event, context):
    params = event["queryStringParameters"]
    print(params)

    # dynamo_manager.create_item("Users", dictionary_item=item)

    return {
        "Success": True,
        "message": [],
        "data": {}
    }

##############################################################################################
