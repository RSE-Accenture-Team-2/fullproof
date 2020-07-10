# Navid-S-B
# lambda handler
# Has basic error checking etc
# Need to add better error checks
# 10-07-2020

import json
import traceback
import serpapi_script as ss

def lambda_handler(event, context):

    image_info = {
        "error": "No",
        "error_type": "None",
        "related_search_term": "None",
        "total_no_results": "None",
        "top_urls": "None",
        "related_key_words": "None"
    }

    try:
        # For AWS Testing
        if type(event) is dict:
            dumped = json.dumps(event)
            event = str(dumped)
        
        jsondata = json.loads(event)
        image_url = jsondata["body"]
        # Adjust response if JSON was sent
        if type(image_url) is str:
            image_url = json.loads(image_url)
            image_url = image_url["image_url"]
        else:
            image_url = image_url["image_url"]

        test_image = ss.serpapi_webpage(image_url)
        image_info['related_search_term'] =  test_image.get_related_search_term()
        image_info['total_no_results'] = test_image.get_no_total_results()
        image_info['top_urls'] = test_image.top_google_urls()
        image_info['related_key_words'] = test_image.get_related_keywords()     

        return {
            'statusCode': 200,
            'body': json.dumps(image_info)
        }

    except Exception as e:

        print(e)
        print(traceback.format_exc())
        return {
            'statusCode' : 500, 
            'body' : json.dumps(traceback.format_exc())
        }
    