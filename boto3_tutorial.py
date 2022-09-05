import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("acooptutorial2")
response = bucket.create(
    ACL='private',
    
)

print(response)