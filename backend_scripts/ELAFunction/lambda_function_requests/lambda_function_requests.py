from bs4 import BeautifulSoup
import requests
import json
import traceback

def lambda_handler(event, context):
    try:
        if type(event) is dict:
            dumped = json.dumps(event)
            event = str(dumped)

        jsondata = json.loads(str(event))
        url = jsondata['body']['url']
        data = { 'url' : url }
        base_url = 'http://fotoforensics.com'
        
        response = requests.post(f'{ base_url }/upload-url.php',data=data)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_endpoint = soup.find(id="MainImg")
        img_endpoint = img_endpoint.attrs["src"]
        img_endpoint = str(img_endpoint).split("&")[0] + "&fmt=ela"
        dns = base_url + img_endpoint
        print("Done")
        return {
        "statusCode": 200,
        "body": json.dumps({ "ELAlink" : dns })
    }
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return {
            'statusCode' : 500, 
            'body' : json.dumps(traceback.format_exc())
 }

event = { 
    "body" : { "url" : "https://images.everydayhealth.com/images/arthritis/lupus/selena-gomez-is-raising-lupus-awareness-rm-722x406.jpg?sfvrsn=7abccc6d_0" }
}
context = None
result = lambda_handler(event, context)
print(result)