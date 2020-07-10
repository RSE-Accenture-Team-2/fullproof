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
import time

class mostFreqTerm():
    params = {
        "engine": None,
        "image_url": None,
        "api_key": None
    }

    image_results = {}

    def __init__(self):
        
        image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/MarioNSMBUDeluxe.png/220px-MarioNSMBUDeluxe.png"
        api_key = "b5cb18a6115e0feb96cadbf0e262de1fd589f2660b51f92b101d4cfd7ef2f7f8"
        engine = "google_reverse_image"

        self.params["engine"] = engine
        self.params["image_url"] = image_url
        self.params["api_key"] = api_key
        client = GoogleSearchResults(self.params)
        results = client.get_dict()
        self.image_results = results['image_results']

        # Collect words and characters from search snippets and titles
        words = []
        for i in range(len(self.image_results)):
            for key, value in self.image_results[i].items():
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

        common_terms = sorted(word_counter, key = word_counter.get, reverse = True)

        print(common_terms[0:5])

         
t1 = time.perf_counter()
hello = mostFreqTerm()
t2 = time.perf_counter()
print(t2-t1)