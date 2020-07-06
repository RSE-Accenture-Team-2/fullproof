# Navid-S-B
# 3-07-2020
"""
Webscraping script to access Google RIS using API Key to gather extra but  
important content not obtainable through the JSON file from the API.
"""

from bs4 import BeautifulSoup
from urllib import request
import re

class serpapi_webpage:

    # Adjust link given
    def __init__(self, image_url):
        
        self.image_url = image_url
        self.api_key = "9103e042e9ebe7ee57d0f91a3a457519932ea82aaf69a778f57721b215c26ff4"
        # Editing link given in for webpage search using REGEX
        p = re.compile('/')
        self.new_url = p.sub("%2F", self.image_url)
        p = re.compile(':')
        self.new_url = p.sub("%3A", self.new_url)
        self.new_url = "https://serpapi.com/search.html?engine=google_reverse_image&image_url={}&api_key={}".format(self.new_url, self.api_key)
        # Optimization made -> load request and soup before analysis
        self.response = request.urlopen(self.new_url).read()
        self.soup = BeautifulSoup(self.response,'html.parser')


    def get_no_total_results(self):

        # Gather html code containing number of searches
        result = str(self.soup.find(id = 'result-stats'))
        # Use REGEX to modify string into returnable number
        p = re.compile('.+s">')
        result = p.sub("", result)
        p = re.compile('<nobr>.*')
        result = p.sub("", result)
        p = re.compile("[^0-9]")
        result = p.sub("", result)
        return int(result)
    
    def get_related_search_term(self):
        
        # Gather html code containing number of searches
        result = str(self.soup.find(class_ = 'fKDtNb'))
        # Use REGEX to get desirable string
        p = re.compile('.*italic">')
        result = p.sub("", result)
        p = re.compile('<.*')
        result = p.sub("", result)
        return result