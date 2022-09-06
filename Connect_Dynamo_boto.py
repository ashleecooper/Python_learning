import boto3

# Connect boto3 to dynamodb

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAQBZM4PDMY23GNNWL', #input access key id
    aws_secret_access_key='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', #input secret key
    )