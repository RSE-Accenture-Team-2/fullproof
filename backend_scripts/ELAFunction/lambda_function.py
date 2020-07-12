from bs4 import BeautifulSoup
import requests
import json
import traceback


def lambda_handler(event, context):
    try:
        print(event)
        if type(event) is not dict:
            eventdata = json.loads(event)
        else:
            eventdata = event
        print(eventdata)
        url = json.loads(eventdata["body"])['url']
        print(url)

        proxies = {
            "https": "103.102.15.90:10714",
            "http": "103.102.15.90:10714"
        }

        data = {'url': url}
        base_url = 'http://fotoforensics.com'
        response = requests.post(
            f'{ base_url }/upload-url.php', data=data, timeout=30, proxies=proxies)

        print(response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_endpoint = soup.find(id="MainImg")
        img_endpoint = img_endpoint.attrs["src"]
        img_endpoint = str(img_endpoint).split("&")[0] + "&fmt=ela"
        dns = base_url + img_endpoint
        return {
            "statusCode": 200,
            "body": json.dumps({'ELAlink': dns})
        }
    except Exception:
        return {
            "statusCode": 500,
            "body": json.dumps(traceback.format_exc())
        }


event = '{ "body" : { "url" : "https://i.insider.com/5ea8734ca34b3c340e3bd55a?width=1800&format=jpeg&auto=webp" } }'
context = None
result = lambda_handler(event, context)
print(result)
