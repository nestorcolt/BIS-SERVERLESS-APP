from Cloud.packages.dynamo import dynamo_manager
from decimal import Decimal
import boto3
import json


##############################################################################################

def lambda_handler(event, context):
    with open("../../tokens.json", "r") as tokens:
        token_data = json.load(tokens)

    for user_id, token in token_data.items():
        item = {

            "user_id": user_id,
            "refresh_token": token,
            "areas": [],
            "search_blocks": True,
            "last_active": Decimal(0.0),
            "speed": Decimal(1.0),
            "minimum_price": Decimal(22.5),
            "search_schedule": []

        }

        dynamo_manager.create_item("Users", dictionary_item=item)
        return


##############################################################################################


def delete_handler(event, context):
    with open("../../tokens.json", "r") as tokens:
        token_data = json.load(tokens)

    for user_id, token in token_data.items():
        dynamo_manager.delete_item("Users", "user_id", user_id)

##############################################################################################

