import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('lambda')


##############################################################################################
def lambda_handler(event, context):
    index = event['iterator']['index'] + 1
    logger.info('Invoke flex active users function:	FlexListActiveUsers')

    response = client.invoke(
        FunctionName='FlexListActiveUsers',
        InvocationType='Event'
    )

    return {
        'index': index,
        'continue': index < event['iterator']['count'],
        'count': event['iterator']['count']
    }

##############################################################################################
