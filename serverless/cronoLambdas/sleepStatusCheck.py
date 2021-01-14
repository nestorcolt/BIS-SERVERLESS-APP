from Cloud.packages.Ec2 import instance_initializer, ec2_manager
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from Cloud.packages import logger
import time
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def sleep_status_check_handler(event, context):
    # Get the records list

    log.info("Cron-lambda")
