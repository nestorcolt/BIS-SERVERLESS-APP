from Cloud.packages.dynamo import modules
import json


##############################################################################################

def lambda_handler(event, context):
    """
    Triggered by an SNS event will put a new entry on the blocks table with the captured blocks from the user.
    This SNS event will be called inside of an Ec2 instance from the search engine
    """
    # Get the records list
    records = event["Records"][0]
    blocks = json.loads(records["Sns"]["Message"])["blocks"]

    for block in blocks:
        modules.put_new_block(block["user_id"], block["data"])
        # TODO better to log this for cloud watch debugging

##############################################################################################
