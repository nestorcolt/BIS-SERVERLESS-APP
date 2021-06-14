from Cloud.packages.aurora import controller
import json

##############################################################################################

conn = controller.connection_handler()


def function_handler(event, context):
    # will query and return aurora data base to get all the users in the platform
    bis_user_list = controller.get_bis_users(conn)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": bis_user_list,
        }),
    }

##############################################################################################
