import sys
import os.path
from PIL import Image, ImageChops, ImageEnhance
import requests
import json
import traceback


def lambda_handler(event, context):
    try:
        filename = sys.argv[1]
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
            # "body": json.dumps({'ELAlink': dns})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(traceback.format_exc())
        }


event = '{ "body" : { "url" : "https://i.insider.com/5ea8734ca34b3c340e3bd55a?width=1800&format=jpeg&auto=webp" } }'
context = None
result = lambda_handler(event, context)
print(result)
