import json
import boto3
from botocore.exceptions import ClientError
import traceback

def lambda_handler(event, context):

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('kanye_quotes')
        
        # when testing the body you test with is easy to decipher
        # when coming from Lambda, you have to get it via event.body
        # and json.loads it into a dict for PUT
        # response = table.put_item( Item=context )
        response = table.put_item( Item=json.loads(event['body']) )
        print(response)
        
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(traceback.format_exc())
        }


