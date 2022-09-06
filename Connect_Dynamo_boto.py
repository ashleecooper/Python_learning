import boto3

# Connect boto3 to dynamodb

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='**********', #input access key id
    aws_secret_access_key='**********', #input secret key
    )
