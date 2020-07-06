# return most freq terms 
# Yinyee 
# 5/07/2020

"""
Webscraping script to find top 3-4 relevant terms from image results
"""

from bs4 import BeautifulSoup
from urllib import request
import re

from serpapi.google_search_results import GoogleSearchResults

class mostFreqTerm():
    params = {
        "engine": None,
        "image_url": None,
        "api_key": None
    }
    image_results = {}
    def __init__(self):
        
        image_url = "https://i.imgur.com/5bGzZi7.jpg"
        api_key = "9103e042e9ebe7ee57d0f91a3a457519932ea82aaf69a778f57721b215c26ff4"
        engine = "google_reverse_image"

        self.params["engine"] = engine
        self.params["image_url"] = image_url
        self.params["api_key"] = api_key
        client = GoogleSearchResults(self.params)
        results = client.get_dict()
        self.image_results = results['image_results']                    
           


hello = mostFreqTerm()
