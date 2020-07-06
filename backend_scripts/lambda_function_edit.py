# Navid-S-B
# 6-07-2020
"""
The lambda function handler is reponsible 
for executing the SerpAPI script in the background.

It has simple error checking measures to ensure smooth execution.

Need to make it look more beautiful.
"""

import json
import serpapi_script as ss

# Check if search link is inputted
def url_error(event):

    # Checks for inputted google search links
    if 'google' in event['image_url']:
        return True
    else:
        return False

# Response if invalid image link is inputted
def url_error_return(event):
   
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

    # Check if request is returned, otherwise release an error
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

# Need to fix this to make it more clean
def lambda_handler(event, context):
    
    # If the url is a google search link
    if url_error(event):
        return url_error_return(event)
    else:
        return execute_code(event)
