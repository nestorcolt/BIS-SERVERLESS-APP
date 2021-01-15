from Cloud.packages.dynamo import controller
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def lambda_handler(event, context):
    """
    Clean up the table blocks from blocks older than 48 hours from the time the function is called
    """
    controller.cleanup_blocks_table()
    log.info("Entries for 'Blocks' table cleaned up successfully")

##############################################################################################
