from Cloud.packages.dynamo import controller as dynamo_controller
from Cloud.packages.s3 import controller as s3_controller
from Cloud.packages.constants import constants as cns


##############################################################################################

def lambda_handler(event, context):
    # update the user stats with the seen offers
    handler_dict = s3_controller.read_users_offers_stats()

    # update dynamo table
    for user, data in handler_dict.items():
        dynamo_controller.update_user_stats(user, validated=data["valid"], offer=data["offers"])

    # delete s3 key object to avoid re count of offers (duplication)
    s3_controller.delete_object_from_bucket(cns.OFFERS_BUCKET_NAME, cns.OFFERS_BUCKET_KEY)

##############################################################################################
