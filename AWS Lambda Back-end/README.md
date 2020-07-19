# fullproof
The best chrome browser extension for image authentication! It utilises the Google Reverse Image Search Engine,</b > 
AWS Rekognition and Error Level Analysis so users can easily authenticate images without switching context.

The Software Architecture is available to see the proposed product MVP.</b >

The following information the extension provides are:

    - No. of Search Results (Serp API)
    - Top 4 Google Image Reverse Search Links (Serp API)
    - Top 4 Related Search Keywords (Serp API)
    - Related Search Term (Serp API)
    - Error level analysis image conversion (Python ELA script)
    - Greatest compression difference in an image (Python ELA script)
    - Object + Label recognition (AWS Rekognition)
    - Celebrity recognition (AWS Rekognition)
    - Text Extraction (AWS Rekognition)

Our ELA Analysis of images has not yet been integrated into a Lambda function to call from the from React front end</b>
however our back end python script produces ELA image conversions from a local file input and a metric for the greatest difference.</b >

Reverse searches through SerpAPI are temporarily disconnected as the prototype was using a trial of the API. ELA works</b >
from the backend script and AWS Rekognition is fully functional however this requires access to our AWS account.</b >

This chrome extension could be further developed in the future, but as of now, it is an inactive project, after</b >
the completion of the Real Skills Education: Steam Leaders Program.</b >

Enjoy exploring!

## SerpAPI Lambda Function
This API is used to scrape Google's Image Reverse Search Engine to extract contextual information</b >
we determined to be important for a user to have a contextual analysis on the image's use</b >
all over the internet.

## ELA Lambda Function
This function is used to digitally analyse a picture to determine the pixel manipulation of</b >
an image. In the current version of the extension, we can generate an ELA image and a metric</b >
which a user can use to determine for themselves if an image has been digitally edited.</b >

## AWS Rekogntion
Scripts related to deep learning through are not found here as the are directly written to AWS lambdas.</b > 

## 
TO NOTE: This is still under development before our first MVP, and may change.

## How We Deploy Our Code
To push our code onto AWS Lambda, we use a virtualenv to replicate and install local python3 libraries which</b >
are not native to AWS Lambda. Some functions are written directly to lambda. In the front end, the app package is 
built to a dist directory which can be installed as the extension. Alternatively running 'npm start' runs the app
in the browser.
