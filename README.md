# fullproof
The best chrome browser extension for image authentication! It utilises the Google Reverse Image Search Engine,</b > 
AWS Rekognition and Error Level Analysis so users can easily authenticate images without switching context.

## Version 1.0.0
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
