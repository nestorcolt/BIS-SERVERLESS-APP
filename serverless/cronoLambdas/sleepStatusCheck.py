from Cloud.packages.Ec2 import instance_initializer, ec2_manager
from Cloud.packages.constants import constants
from Cloud.packages.utilities import utils
from Cloud.packages.dynamo import modules
from Cloud.packages import logger
import boto3
import time
import json

LOGGER = logger.Logger(__name__)
log = LOGGER.logger


##############################################################################################

def sleep_status_check_handler(event, context):
    last_active = modules.get_last_active_users()

    for user in last_active:
        print(user)

