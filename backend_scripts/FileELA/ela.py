import sys
import os.path
from PIL import Image, ImageChops, ImageEnhance
import requests
import json
import traceback
import base64


def baseConversion(image_in):

    try:
        imgdata = base64.b64decode(image_in)
        filename = 'tmp/input.jpg'
        print(f"data is {imgdata}")
        with open(filename, 'w') as f:
            f.write(imgdata)

        im = Image.open(f'/tmp/input.jpg')
        im.show()
        print("done")
        return filename

    except Exception:
        return {
            "statusCode": 777,
            "body": json.dumps(traceback.format_exc())
        }


def lambda_handler(event, context):
    event = json.loads(event)['body']
    image_in = event['image_64']
    print(f"Image in is... {image_in}")
    filename = baseConversion(image_in)

    try:
        resaved = filename + '.resaved.jpg'
        ela = filename + '.ela.png'
        im = Image.open(filename)

        im.save(resaved, 'JPEG', quality=95)
        resaved_im = Image.open(resaved)

        ela_im = ImageChops.difference(im, resaved_im)
        extrema = ela_im.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        scale = 255.0/max_diff

        ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)

        print(F"Maximum difference was {max_diff}")
        ela_im.save(ela)
        ela_im.show()

        return {
            "statusCode": 200,
            "body": "code ran wowo!!"
        }
    except Exception:
        return {
            "statusCode": 500,
            "body": json.dumps(traceback.format_exc())
        }


event = '{ "body" : { "image_64" : "LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5UUd0bjZyYVowNHEwdDJtdA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJbb2JqZWN0IEZpbGVdIg0KDQp1bmRlZmluZWQNCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeVFHdG42cmFaMDRxMHQybXQNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0idW5kZWZpbmVkIg0KDQp1bmRlZmluZWQNCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeVFHdG42cmFaMDRxMHQybXQNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0idW5kZWZpbmVkIg0KDQp1bmRlZmluZWQNCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeVFHdG42cmFaMDRxMHQybXQtLQ0K" } }'
context = None
result = lambda_handler(event, context)
print(result)

# "body": json.dumps({'ELAlink': dns})
