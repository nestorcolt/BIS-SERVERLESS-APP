import boto3
import json

##############################################################################################

TARGET_LAYER_NAME = "DotnetCloudLibrary"


def function_handler(event, context):
    layer_version = get_latest_layer()
    fragment = event['fragment']
    fragment["Layers"] = [layer_version]

    return {
        'requestId': event['requestId'],
        'status': 'success',
        'fragment': fragment
    }


##############################################################################################
def get_latest_layer():
    client = boto3.client('lambda')
    layers = client.list_layers(
        CompatibleRuntime='dotnetcore3.1',
        MaxItems=10
    )

    response = layers["Layers"]
    if response:
        for itm in response:
            name = itm["LayerName"]

            if name == TARGET_LAYER_NAME:
                match = itm["LatestMatchingVersion"]
                arn = match["LayerVersionArn"]
                return arn

##############################################################################################
