# Navid-S-B
# 3-07-2020
"""
Webscraping script to access Google RIS using API Key to gather extra but  
important content not obtainable through the JSON file from the API.
"""

from bs4 import BeautifulSoup
import urllib
import json
import re

class serpapi_webpage:

    # Adjust link given
    def __init__(self, image_url):
        
        self.image_url = image_url
        api_key = "9103e042e9ebe7ee57d0f91a3a457519932ea82aaf69a778f57721b215c26ff4"
        # Editing link given in for webpage search using REGEX
        p = re.compile('/')
        new_url = p.sub("%2F", self.image_url)
        p = re.compile(':')
        new_url = p.sub("%3A", new_url)
        new_url = "https://serpapi.com/search.html?engine=google_reverse_image&image_url={}&api_key={}".format(new_url, api_key)
        # Optimization made -> load request and soup before analysis
        response = urllib.request.urlopen(new_url).read()
        self.soup = BeautifulSoup(response,'html.parser')
        # Load JSon File from SerpAPI for analysis
        json_link = "https://serpapi.com/search.json?engine=google_reverse_image&google_domain=google.com&image_url={}&api_key={}".format(new_url, api_key)
        json_link = urllib.request.urlopen(json_link)
        json_data = json.loads(json_link.read())
        self.image_results = json_data['image_results']        

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
        result = str(self.soup.find(class_ = "fKDtNb"))
        # Use REGEX to get desirable string
        p = re.compile('.*italic">')
        result = p.sub("", result)
        p = re.compile('<.*')
        result = p.sub("", result)
        return result
    
    def top_google_urls(self):
        url_list = []
        for i in range(len(self.image_results)):
            for key, value in self.image_results[i].items():
                if(key == "link"):
                    url_list.append(value)
        
        return url_list
    
    def get_related_keywords(self):
        pass


image_link = "https://pyxis.nymag.com/v1/imgs/3b6/d67/84797c3613ee95604b9262ce0823c67a2e-21-selena-gomez.rsquare.w1200.jpg"
webpage = serpapi_webpage(image_link)
url_list = webpage.top_google_urls()
print(url_list)


