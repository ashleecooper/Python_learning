#Week 15-Create SQS queue using Python

import boto3

sqs = boto3.resource('sqs')

#When queue is created it will print an instance
queue = sqs.create_queue(QueueName='ACoop_wk15_queue')

print(queue.url)