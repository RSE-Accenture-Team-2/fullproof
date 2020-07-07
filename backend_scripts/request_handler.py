import json
import requests

def request_handler(event, context):

    api_key = "9103e042e9ebe7ee57d0f91a3a457519932ea82aaf69a778f57721b215c26ff4"
    json_link = "https://serpapi.com/search.json?engine=google_reverse_image&google_domain=google.com&image_url={}&api_key={}".format(event['image_url'], api_key)
    json_data = requests.get(json_link).json()

    # TODO implement
    return {
        'statusCode': 200,
        'body': json_data
    }
