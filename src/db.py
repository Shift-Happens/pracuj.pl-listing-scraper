import boto3
import json
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'job_offers'

def create_table():
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        logger.info(f"Created table {table_name}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info(f"Table {table_name} already exists")
        else:
            logger.error(f"Error creating table: {str(e)}")
            raise

def add_or_update_offers(offers):
    table = dynamodb.Table(table_name)
    new_offers = []
    
    for offer in offers:
        try:
            response = table.get_item(Key={'id': offer['id']})
            if 'Item' not in response:
                table.put_item(Item={
                    'id': offer['id'],
                    'title': offer['title'],
                    'company': offer['company'],
                    'technologies': offer['technologies'],
                    'salary': offer['salary'],
                    'work_modes': offer['work_modes'],
                    'contract_types': offer['contract_types'],
                    'workplace': offer['workplace']
                })
                new_offers.append(offer)
                logger.info(f"Added new offer: {offer['title']}")
        except ClientError as e:
            logger.error(f"Error processing offer {offer['id']}: {str(e)}")
            
    return new_offers