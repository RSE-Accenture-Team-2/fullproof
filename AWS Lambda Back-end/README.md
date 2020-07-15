# fullproof: The AWS Lambda Back-End
These are the backend scripts for the python3 lambda functions which use different services/functions</b >
to extract and uncover information about an image.

## SerpAPI Lambda Function
This API is used to scrape Google's Image Reverse Search Engine to extract key information</b >
we determined to be important for a user to have a contextual analysis on the image's use</b >
all over the internet.

## ELA Lambda Function
This function is used to digitally analyse a picture to determine the pixel manipulation of</b >
an image. However in the current version of the extension, we have only managed to generate</b >
an ELA image and a metric which a user can use to determine for themselves if an image has</b >
been digitally edited.

## Future Functionality
Hopefully this extension is expanded and can calculate a confidence threshold to determine the</b >
the likelihood of image manipulation for a better user experience. This would be likely through </b >
expanding our features to use sentiment analysis on a picture and the context the picture is used</b >
in, applying a ML model to determine image manipulation and utilising blockchain technology for a</b >
database of reliable images to compare against.

## 
TO NOTE: This is still under development before our first MVP, and may change.

## How We Deploy Our Code
To push our code onto AWS Lambda, we use a virtualenv to replicate and install local python3 libraries which</b >
are not native to AWS Lambda. 
