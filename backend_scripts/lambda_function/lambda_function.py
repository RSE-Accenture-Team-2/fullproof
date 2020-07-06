# Navid-S-B
# 6-07-2020
"""
The lambda function handler is reponsible 
for executing the SerpAPI script in the background.
Currently it checks for one possible link error where a google
link instead of an actual image link. 

Otherwise if a request cannot be made, it releases the Standard
"""

import json
import serpapi_script as ss

def url_error(event):

    # Checks for inputted google search links
    if 'google' in event['image_url']:
        return True
    else:
        return False

def execute_code(event):
    
    # Add dictionary
    image_info = {
        "error": "No",
        "error_type": "None",
        "related_search_term": "None",
        "total_no_results": "None",
        "top_links": "None",
        "related_key_words": "None"
    }

    try:
        test_image = ss.serpapi_webpage(event["image_url"])
        image_info["related_search_term"] = test_image.get_related_search_term()
        image_info["total_no_results"] = test_image.get_no_total_results()
        return {
            'statusCode': 200,
            'body': json.dumps(image_info)
        }

    except:
        image_info["error"] = "Yes"
        image_info["error_type"] = "Image Search Failed"
        return {
            'statusCode': 500,
            'body': json.dumps(image_info)
        }

def lambda_handler(event, context):
    
    if url_error(event):

        image_info = {
            "error": "Yes",
            "error_type": "Invalid Image URL",
            "related_search_term": "None",
            "total_no_results": "None",
            "top_links": "None",
            "related_key_words": "None"
        } 

        return {
            'statusCode': 500,
            'body': json.dumps(image_info)
        }

    else:
        return execute_code(event)
