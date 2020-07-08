# return most freq terms 
# Yinyee 
# 5/07/2020
# Navid-S-B
# 8/07/2020

"""
Analysing a JSON input containing image search data
to find top 5-10 relevant terms from title knowledge graph title or image results.

Uses textblob to only capture phrases with nouns.
Possible sentiment extension from this function
"""

from serpapi.google_search_results import GoogleSearchResults
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import time

class mostFreqTerm():
    params = {
        "engine": None,
        "image_url": None,
        "api_key": None
    }

    image_results = {}

    def __init__(self):
        
        image_url = "https://static.scientificamerican.com/sciam/cache/file/5C51E427-1715-44E6-9B14D9487D7B7F2D_source.jpg"
        api_key = "b5cb18a6115e0feb96cadbf0e262de1fd589f2660b51f92b101d4cfd7ef2f7f8"
        engine = "google_reverse_image"

        self.params["engine"] = engine
        self.params["image_url"] = image_url
        self.params["api_key"] = api_key
        client = GoogleSearchResults(self.params)
        results = client.get_dict()
        self.image_results = results['image_results']

        # Use textblob to remove noun phrases from the titles and snippets of 
        # google reverse image search results.
        extractor = ConllExtractor()
        phrases = []
        for i in range(len(self.image_results)):
            for key, value in self.image_results[i].items():
                if (key == "title" or key == 'snippet'):
                    # Extract phrases containing nouns
                    blob = TextBlob(value, np_extractor=extractor)
                    # Convert WordList obj to a list
                    phrases += list(blob.noun_phrases)

        # Split phrases to isolate words and remove non-word characters
        word = []
        for k in phrases:
            for i in k.split():
                if i in ["|",":","'",'"','%','?','(',')']:
                    continue
                word.append(i)

        # Utilise a hash map to count most frequent nouns
        word_counter = {}
        for i in word:
            if i in word_counter:
                word_counter[i]+= 1
            else:
                word_counter[i] = 1

        common_terms = sorted(word_counter, key = word_counter.get, reverse = True)
        print(common_terms[:5])

         
t1 = time.perf_counter()
hello = mostFreqTerm()
t2 = time.perf_counter()
print(t2-t1)