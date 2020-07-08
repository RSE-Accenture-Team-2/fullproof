from bs4 import BeautifulSoup
import requests
import json

def lambda_handler(event, context):
    data = { 'url' : event['body']['url'] }
    base_url = 'http://fotoforensics.com'
    response = requests.post(f'{ base_url }/upload-url.php',data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_endpoint = soup.find(id="MainImg")
    img_endpoint = img_endpoint.attrs["src"]
    img_endpoint = str(img_endpoint).split("&")[0] + "&fmt=ela"
    dns = base_url + img_endpoint
    return {
    "statusCode": 200,
    "body": json.dumps({ "ELAlink" : dns })
    }

