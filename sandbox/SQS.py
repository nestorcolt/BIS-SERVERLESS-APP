from Cloud.packages.constants import constants
from Cloud.packages.sqs import sqs_manager
from datetime import datetime
from pprint import pprint
import boto3
import time
import json
client = boto3.client("sqs")

# response = client.send_message(
#     QueueUrl=r'https://sqs.us-east-1.amazonaws.com/320132171574/GetUserBlocksQueue',
#     MessageBody='{"user_id": "15"}',
#     DelaySeconds=1,
# )

# now = datetime.now()
# print(now.strftime("%d/%m/%Y %H:%M:%S"))
# time.sleep(0.4)

# user_id = "15"

for index in range(100):
    messages = sqs_manager.get_messages_from_queue("SE_FIFO.fifo")
    print(messages)
    # result = list(map(lambda itm: json.loads(itm["Body"]).get(constants.TABLE_PK) == user_id, messages))
    # print(result)
    print(index)
    # time.sleep(1)
