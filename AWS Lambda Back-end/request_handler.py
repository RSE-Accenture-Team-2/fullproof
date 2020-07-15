import json
import urllib.request
import urllib.parse
import re

def request_handler(image_url):

    api_key = "api_key"
    p = re.compile('/')
    new_url = p.sub("%2F", image_url)
    p = re.compile(':')
    new_url = p.sub("%3A", new_url)
    new_link = "https://serpapi.com/search.json?engine=google_reverse_image&google_domain=google.com&image_url={}&api_key={}".format(new_url, api_key)
    f = urllib.request.urlopen(new_link)
    new_json = json.loads(f.read().decode('utf-8'))
    new_json = new_json['image_results']

    url_list = []
    for i in range(len(new_json)):
        for key, value in new_json[i].items():
            if(key == "link"):
                url_list.append(value)

    print(url_list)


image_link = "https://cdn.eso.org/images/thumb300y/eso1907a.jpg"
request_handler(image_link)

