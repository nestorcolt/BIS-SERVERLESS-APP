from Cloud.packages.dynamo import controller
from Cloud.packages import logger
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def function_handler(event, context):
    # Get the records list
    records = event["Records"][0]
    user_id = json.loads(records["Sns"]["Message"])

    try:
        if user_id:
            # update dynamo DB
            controller.set_last_active_user_time(str(user_id))

    except Exception as e:
        # Send some context about this error to Lambda Logs
        log.error(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"User: {user_id} has been sent to sleep for 30 minutes",
        }),
    }

##############################################################################################