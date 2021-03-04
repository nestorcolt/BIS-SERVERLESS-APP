from datetime import datetime
import boto3
import time

client = boto3.client("sqs")

for index in range(10):
    response = client.send_message(
        QueueUrl=r'https://sqs.us-east-1.amazonaws.com/320132171574/TestStartSeQ',
        MessageBody='{"user_id"}: "12',
        DelaySeconds=1,
    )

    now = datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(0.4)