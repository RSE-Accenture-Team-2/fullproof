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
        self.search_url = 'https://www.google.com/searchbyimage?&image_url={}'.format(image_url)

    # Get number of results
    # Can't seem to extract the number of results information using soup.find or soup.find_all?
    def get_no_results(self):

        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text,'html.parser')
        no_results = soup.find(id="result-stats")
        print(no_results)


webpage = RIS_scraper('cuyastro.files.wordpress.com/2020/04/hubble-at-30_heic2007a.jpg?w=1024')
webpage.get_no_results()