from Cloud.packages.constants import constants
from Cloud.packages.dynamo import controller
from aws_lambda_powertools import Tracer
from Cloud.packages import logger

LOGGER = logger.Logger(__name__)
log = LOGGER.logger

##############################################################################################
tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Clean up the table blocks from blocks older than 48 hours from the time the function is called
    """
    controller.cleanup_blocks_table()
    controller.cleanup_offers_table()
    log.info(f"Entries over {constants.CLEANUP_BLOCKS_TIME_THRESHOLD} hours removed from tables:\n-Blocks\n-Offers")

##############################################################################################
