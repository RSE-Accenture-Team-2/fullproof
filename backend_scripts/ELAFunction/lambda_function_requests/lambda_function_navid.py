from bs4 import BeautifulSoup
import requests
import json
import re

def lambda_handler(event, context):
    data = { 'url' : event['body']['url'] }
    base_url = 'http://fotoforensics.com/'
    response = requests.post(f"{ base_url }upload-url.php",data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_endpoint = str(soup.find(id="MainImg"))
    p = re.compile('.+" src="/')
    img_endpoint = p.sub("", img_endpoint)
    p = re.compile('&.+$')
    img_endpoint = p.sub("", img_endpoint)
    dns = base_url + img_endpoint + '&fmt=ela'
    return {
    "statusCode": 200,
    "body": json.dumps({ "ELAlink" : dns })
    }