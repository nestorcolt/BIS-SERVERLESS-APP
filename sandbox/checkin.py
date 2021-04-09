from Cloud.packages.controller import check_in_controller
from Cloud.packages.controller import user_controller

##############################################################################################
user_id = "5"
user_data = user_controller.get_user_data({"user_id": user_id})
refresh_token = user_data["refresh_token"]
access_token = user_controller.get_access_token(refresh_token)
user_controller.get_schedule(access_token, refresh_token)
