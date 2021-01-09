from Cloud.packages.constants import constants
import requests
import boto3
import json


##############################################################################################

def lambda_handler(event, context):
    # these modules are imported in a package layer
    print(requests)
    print(boto3)
    print(dir(constants))

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        print(ip.content)
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }
