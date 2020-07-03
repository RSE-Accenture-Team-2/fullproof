# Navid Bhuiyan 
# 3-07-2020
# Webscraping script to access TinEye
# UPDATE: Same problem, cannot download whole HTML script to scrape webpage.
# Must have some kind of protective measure so people use their API instead.

# Import webscraping libraries
from bs4 import BeautifulSoup
import requests
import re

class scraper:

    def __init__(self, image_url):
        
        self.image_url = image_url
        p = re.compile('/')
        self.new_url = p.sub("%2F", self.image_url)
        p = re.compile(':')
        self.new_url = p.sub("%3A", self.new_url)
        self.new_url = "http://www.tineye.com/search/?url{}".format(self.new_url)
    
    def get_no_results(self):

        response = requests.get(self.new_url)
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)


webpage = scraper("https://cdn.spacetelescope.org/archives/images/wallpaper2/heic2007a.jpg")
webpage.get_no_results()