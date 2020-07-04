import json
import serpapi_script as ss

def lambda_handler(event, context):
    # TODO implement
    test_image = ss.serpapi_webpage('https://s1.at.atcdn.net/wp-content/uploads/2018/09/Uluru_hero-768x369.jpg')
    search_term = test_image.related_search_term()


    return {
        'statusCode': 200,
        'body': json.dumps(search_term)
    }