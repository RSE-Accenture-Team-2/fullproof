from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import json
import traceback

def lambda_handler(event, context):
    try:
        if type(event) is dict:
            dumped = json.dumps(event)
            event = str(dumped)

        jsondata = json.loads(str(event))
        print(type(jsondata))
        print(jsondata)

        url = jsondata['body']['url']
        # data = { 'url' : url }
        base_url = 'http://fotoforensics.com'

        url = base_url
        full_url = url + '?url=' + url
        response = urllib.request.urlopen(full_url)

        # response = requests.post(f'{ base_url }/upload-url.php',data=data)
        print(response)

        soup = BeautifulSoup(response, 'html.parser')
        img_endpoint = soup.find(id="MainImg")
        img_endpoint = img_endpoint.attrs['src']
        img_endpoint = str(img_endpoint).split("&")[0] + "&fmt=ela"
        dns = base_url + img_endpoint
        print(dns)
        return {
        "statusCode": 200,
        "body": { 'ELAlink' : dns }
    }
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return {
            'statusCode' : 500, 
            'body' : json.dumps(traceback.format_exc())
 }

event = { "body" : { "url" : "https://i.insider.com/5ea8734ca34b3c340e3bd55a?width=1800&format=jpeg&auto=webp" } }
context = None
result = lambda_handler(event, context)
print(result)