# Navid Bhuiyan 
# 3-07-2020
# Webscraping script to access google reverse search
# Currently need to extract number of results data


# Import webscraping libraries
from bs4 import BeautifulSoup
import requests
import re


class RIS_scraper:

    def __init__(self, image_url):
        
        self.image_url = image_url
        self.search_url = ' https://www.google.com/searchbyimage?&image_url={}'.format(image_url)

    # Get number of results
    # Can't seem to extract the number of results information using soup.find or soup.find_all?
    def get_no_results(self):

        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)


webpage = RIS_scraper('3iom3142cnb81rlnt6w4mtlr-wpengine.netdna-ssl.com/wp-content/uploads/2019/04/fig1-6.jpg')
webpage.get_no_results()