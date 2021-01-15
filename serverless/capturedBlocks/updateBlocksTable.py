from Cloud.packages.dynamo import modules
import json


##############################################################################################

def lambda_handler(event, context):
    """
    Clean up the table blocks from blocks older than 48 hours from the time the function is called
    """
    # Get the records list
    records = event["Records"][0]
    blocks = json.loads(records["Sns"]["Message"])["blocks"]

    for block in blocks:
        modules.put_new_block(block["user_id"], block["data"])
        # TODO better to log this for cloud watch debbuging

##############################################################################################
