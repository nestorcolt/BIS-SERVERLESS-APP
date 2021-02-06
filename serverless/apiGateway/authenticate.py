from Cloud.packages.security import api_security
import json


##############################################################################################
def function_handler(event, context):
    """

    Authenticate and get the refresh and access token

    """
    status_code = 200

    try:
        response = api_security.authenticate_and_get_token(event)

    except Exception as e:
        status_code = 410
        response = e.__str__()

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": response,
        }),
    }

##############################################################################################
