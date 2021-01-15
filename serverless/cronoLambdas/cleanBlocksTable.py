from Cloud.packages.dynamo import modules


##############################################################################################

def lambda_handler(event, context):
    """
    Clean up the table blocks from blocks older than 48 hours from the time the function is called
    """
    modules.cleanup_blocks_table()

##############################################################################################
