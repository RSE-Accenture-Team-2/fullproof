from bs4 import BeautifulSoup
from urllib import request
import re
import webbrowser
import json

def lambda_handler(event, context):
    jsondata = json.loads(event["body"])
    url = jsondata['url']
    html_page = request.urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    return {
	"statusCode": 200,
     "body": json.dumps({'links_list' : images})
}