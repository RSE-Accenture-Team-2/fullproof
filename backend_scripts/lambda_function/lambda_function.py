import json
import serpapi_script as ss

def lambda_handler(event, context):
    # Error checking
    try:
        test_image = ss.serpapi_webpage(event['image_url'])
        search_term = test_image.get_related_search_term()
        no_results = test_image.get_no_total_results()
        return {
            'statusCode': 200,
            'body': json.dumps({'related_search_term':search_term,'total_no_results':no_results}, 
                                sort_keys=True, indent=4)
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('Image search failed')
        }