import json
import serpapi_script as ss

def lambda_handler(event, context):
    
    # Basic error test, need to detect false urls being added.
    # Also add some time function to enable except to be executed
    try:
        test_image = ss.serpapi_webpage(event['image_url'])
        search_term = test_image.get_related_search_term()
        no_results = test_image.get_no_total_results()
        return {
            'statusCode': 200,
            'body': {"related_search_term":search_term,"total_no_results":no_results}
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps("Image search failed")
        }