import json
import boto3
from botocore import UNSIGNED
from botocore.client import Config

class SQS_client:
    def __init__(self, debug=False):
        # Set the AWS region and queue URL (in this case, a local SQS queue)
        self.AWS_REGION = 'us-east-1'
        self.QUEUE_URL = 'http://localhost:4566/000000000000/login-queue'
        self.sqs = boto3.client('sqs', endpoint_url=self.QUEUE_URL, region_name=self.AWS_REGION, config=Config(signature_version=UNSIGNED))
        self.debug = True

    def connect(self):
        pass 

    def disconnect(self):
        self.sqs.close()

    def read_queue(self):
        response = self.sqs.receive_message(
            QueueUrl=self.QUEUE_URL,
            AttributeNames=['All'],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=1
        )

        if self.debug:
            print("\n Response from Queue:\n", response)

        if "Messages" not in response:
            print("\n NO MORE MESSAGES!")
            return None

        messages = [json.loads(message['Body']) for message in response['Messages']]
        return messages
