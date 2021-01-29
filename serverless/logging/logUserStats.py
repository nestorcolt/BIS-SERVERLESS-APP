from Cloud.packages.cloudwatch import logs_manager


##############################################################################################

def lambda_handler(event, context):
    # LOG TO CLOUDWATCH ALL USERS WITH STATUS SEARCHING
    logs_manager.log_all_users()

##############################################################################################
