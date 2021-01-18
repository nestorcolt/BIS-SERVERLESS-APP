from Cloud.packages.dynamo import dynamo_manager
from decimal import Decimal
import boto3
import json


##############################################################################################

def function_handler(event, context):
        return {
                "success": True,
                "message": [],
                "data": event
        }


##############################################################################################
