from Cloud.packages.controller import check_in_controller
from Cloud.packages.controller import user_controller
import time

##############################################################################################
user_id = "12"


user_data = user_controller.get_user_data({"user_id": user_id})
refresh_token = user_data["refresh_token"]
access_token = user_controller.get_access_token(refresh_token)
user_controller.get_schedule(access_token, refresh_token)

# def is_block_check_in(block_time):
#     current_time = int(time.time())
#     block_start_time = block_time + 300
#
#     if block_start_time - current_time <= 20 * 60:
#         return True
#
#     return False
#
#
# block_time_id = 1617998400.0
# print(is_block_check_in(block_time_id))
