import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 

# Create your table
table = dynamodb.create_table(
    TableName='Netflix_Top_10', #enter table name
    KeySchema=[
        {
            'AttributeName': 'ranking', 
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ranking',
            'AttributeType': 'N'  #number
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'  #string
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status) 