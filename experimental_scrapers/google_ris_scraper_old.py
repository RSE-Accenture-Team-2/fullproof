# Navid-S-B 
# 3-07-2020
# Webscraping script to access google reverse search
# Currently need to extract number of results data
# UPDATE: not a long term solution, TinEye API has to be better.
# not using this.


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
    # When I used egrep to find if the html downloaded by soup contains the result, it did not come at all?
    def get_no_results(self):

        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text,'html.parser')
        # no_results = soup.find(id="result-stats")
        print(soup)


webpage = RIS_scraper('https://cdn.pixabay.com/photo/2015/02/24/15/41/dog-647528_1280.jpg')
webpage.get_no_results()