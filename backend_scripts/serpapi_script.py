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
        api_key = "b5cb18a6115e0feb96cadbf0e262de1fd589f2660b51f92b101d4cfd7ef2f7f8"
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
        return 'None'


# Old get_related_keywords_code
"""
# Use textblob to remove noun phrases from the titles and snippets of 
# google reverse image search results.
extractor = ConllExtractor()
phrases_with_nouns = []
for i in range(len(self.image_results_json)):
    for key, value in self.image_results_json[i].items():
        if (key == "title" or key == 'snippet'):
            # Extract phrases containing nouns
            blob = TextBlob(value, np_extractor=extractor)
            # Convert WordList obj to a list
            phrases_with_nouns += list(blob.noun_phrases)

# Split phrases to isolate nouns and remove non-word characters
nouns = []
for k in phrases_with_nouns:
    for i in k.split():
        if i in ["|",":","'",'"','%','?','(',')']:
            continue
        nouns.append(i)

# Utilise a hash map to count most frequent nouns
word_counter = {}
for i in nouns:
    if i in word_counter:
        word_counter[i]+= 1
    else:
        word_counter[i] = 1

# Sort words by count and get top five terms
common_terms = sorted(word_counter, key = word_counter.get, reverse = True)
return common_terms[0:5]
"""