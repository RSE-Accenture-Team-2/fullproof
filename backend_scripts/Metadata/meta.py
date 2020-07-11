import requests
import json
import traceback


def lambda_handler(event, context):
    try:
        print("hello")
        return {
            "statusCode": 200,
            "body": json.dumps({'ELAlink': dns})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(traceback.format_exc())
        }


event = '{ "body" : { "url" : "https://i.insider.com/5ea8734ca34b3c340e3bd55a?width=1800&format=jpeg&auto=webp" } }'
context = None
result = lambda_handler(event, context)
print(result)
