from Cloud.packages.dynamo import dynamo_manager
from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller


######################################################


def function_handler():
    """
    Checks for an attribute name "last_active" and if the time span is greater than 30 minutes ago from now
    will start the instance with the user ID
    :return:
    """
    last_active = controller.get_all_users()

    for user_data in last_active["Items"]:
        user_id = user_data["user_id"]
        update_item = {"search_blocks": False}
        dynamo_manager.update_item("Users", "user_id", user_id, update_item)


def switch_user_state(user_id, value):
    dynamo_manager.update_item("Users", "user_id", user_id, {"search_blocks": value})


##############################################################################################
if __name__ == '__main__':
    # function_handler()
    switch_user_state("5", False)
