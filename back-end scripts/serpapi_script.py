# Navid-S-B
# 3-07-2020
"""
Webscraping script to access Google RIS using API Key to gather extra but  
important content not obtainable through the JSON file from the API.
"""

from bs4 import BeautifulSoup
import urllib.request
import json
import re

class serpapi_webpage:

    # Adjust link given
    def __init__(self, image_url):
        
        # Enter API key
        api_key = "add_key"
        # Editing link given in for webpage search using REGEX
        p = re.compile('/')
        image_url = p.sub("%2F", image_url)
        p = re.compile(':')
        image_url = p.sub("%3A", image_url)
        new_url = "https://serpapi.com/search.html?engine=google_reverse_image&image_url={}&api_key={}".format(image_url, api_key)
        # Optimization made -> load request and soup before analysis
        response = urllib.request.urlopen(new_url).read()
        self.soup = BeautifulSoup(response,'html.parser')
        # Saving JSON output from API
        json_link = "https://serpapi.com/search.json?engine=google_reverse_image&google_domain=google.com&image_url={}&api_key={}".format(image_url, api_key)
        response = urllib.request.urlopen(json_link)
        json_response = json.loads(response.read().decode('utf-8'))
        self.image_results_json = json_response['image_results']

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
        
        # Go through dictionary and loop through for first page links
        url_list = []
        for i in range(len(self.image_results_json)):
            for key, value in self.image_results_json[i].items():
                if(key == "link"):
                    url_list.append(value) 
        return url_list
    

    def get_related_keywords(self):
        # Collect words and characters from search snippets and titles
        words = []
        for i in range(len(self.image_results_json)):
            for key, value in self.image_results_json[i].items():
                if (key == "title" or key == 'snippet'):
                    words = words + value.split()

        # Word filter (this is only implemented as a concept)
        # There is another version where this uses textblob to only detect nouns
        # Remove characters and common conjunction
        for word in words:
            word_lower = word.lower()
            # Remove common characters
            for char in ("|",":","'",'"','%','?','(',')','...','.', '-'):
                if word == char:
                    words.pop(words.index(word))
            # Remove common conjunctions
            for conj in ('and', 'nor', 'but', 'yet', 'so' ):
                if word_lower == conj:
                    words.pop(words.index(word))
            # Remove common prepositions
            for prep in ('above', 'across', 'against', 'along', 'among', 'around', 'at', 'before', 
            'behind', 'below', 'beneath', 'beside', 'between', 'by', 'down', 'from', 'in', 'into', 
            'near', 'of', 'off', 'on', 'to', 'toward', 'under', 'upon', 'within'):
                if word_lower == prep:
                    words.pop(words.index(word))
        
        # Remove common verbs, articles, pronouns i.e. second filtration
        for word2 in words:
            word2_lower = word2.lower()
            # Remove common verbs, articles, and prepositions
            for mixed_word in ('are', 'is', 'a', 'an', 'the', 'they', 'for'):
                if word2_lower == mixed_word:
                    words.pop(words.index(word2))
        
        # Utilise a hash map to count most frequent nouns
        word_counter = {}
        for i in words:
            if i in word_counter:
                word_counter[i] += 1
            else:
                word_counter[i] = 1

        # Get top 5 related keywords
        related_keywords = sorted(word_counter, key = word_counter.get, reverse = True)
        related_keywords = related_keywords[:5]
        return related_keywords
