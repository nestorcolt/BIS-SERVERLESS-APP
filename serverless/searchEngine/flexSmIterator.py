import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('lambda')


##############################################################################################
def lambda_handler(event, context):
    index = event['iterator']['index'] + 1
    logger.info('Invoke flex active users function:	flex-list-active-users')

    response = client.invoke(
        FunctionName='flex-list-active-users',
        InvocationType='Event'
    )

    return {
        'index': index,
        'continue': index < event['iterator']['count'],
        'count': event['iterator']['count']
    }

##############################################################################################
