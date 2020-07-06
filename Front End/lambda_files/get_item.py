import json
import boto3
from botocore.exceptions import ClientError
import random

def lambda_handler(event, context):

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('kanye_quotes')
        
        table_data = table.scan()
        print(table_data)
        random_number = random.randrange(table_data['Count'])
        print(random_number)
        quote = table_data['Items'][random_number]
        
        return {
            'statusCode': 200,
            'body': json.dumps(quote)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(e.response['Error']['Message'])
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }

