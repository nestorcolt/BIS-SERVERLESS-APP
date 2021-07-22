from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller


##############################################################################################


def function_handler(event, context):
    """
    Get all users available un the Users table and will set the atomic counters back to zero every
    24 hours. Meaning: every 0:00:00 from every day UTC
    """
    # Get the records list
    users = controller.get_all_users_in_stats_table()

    for user_data in users["Items"]:
        user = user_data[constants.TABLE_PK]
        controller.reset_user_stats(user)

##############################################################################################
