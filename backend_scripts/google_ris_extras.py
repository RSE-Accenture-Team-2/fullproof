# Navid-S-B
# 3-07-2020
# Webscraping script to access Google RIS using API Key to gather extra but 
# important content not found in the original RespAPI json file

# Import webscraping libraries
from bs4 import BeautifulSoup
import requests
import re

class extra_info:

    # Adjust link given
    def __init__(self, image_url):
        
        self.image_url = image_url
        self.api_key = "29a07d0e5f60d19ed0715a8910049126ae62bbb3a49ecfb60957873e7e0c9248"
        # Editing link given in for webpage search
        p = re.compile('/')
        self.new_url = p.sub("%2F", self.image_url)
        p = re.compile(':')
        self.new_url = p.sub("%3A", self.new_url)
        self.new_url = "https://serpapi.com/search.html?engine=google_reverse_image&image_url={}&&api_key={}".format(self.new_url, self.api_key)
    
    def get_no_total_results(self):

        # Get webpage
        response = requests.get(self.new_url)
        soup = BeautifulSoup(response.text,'html.parser')
        # Gather html code containing number of searches
        result = str(soup.find(id = 'result-stats'))
        # Use REGEX to modify string into returnable number
        p = re.compile('.+s">')
        result = p.sub("", result)
        p = re.compile('<nobr>.*')
        result = p.sub("", result)
        p = re.compile("[^0-9]")
        result = p.sub("", result)
        return int(result)
    
    def related_search_term(self):
        
        # Get webpage
        response = requests.get(self.new_url)
        soup = BeautifulSoup(response.text,'html.parser')
        # Gather html code containing number of searches
        result = str(soup.find(class_ = 'fKDtNb'))
        # Use REGEX to get desirable string
        p = re.compile('.*italic">')
        result = p.sub("", result)
        p = re.compile('<.*')
        result = p.sub("", result)
        return result

def lambda_handler(event, context):
# TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
