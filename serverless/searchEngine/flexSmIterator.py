from aws_lambda_powertools import Tracer
import boto3

client = boto3.client('lambda')

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def function_handler(event, context):
    index = event['iterator']['index'] + 1

    client.invoke(
        FunctionName='FlexListActiveUsers',
        InvocationType='Event'
    )

    return {
        'index': index,
        'continue': index < event['iterator']['count'],
        'count': event['iterator']['count']
    }

##############################################################################################
