# fullproof: The Development of the Software
These are all of our Software Architecture Diagrams that were made during our project.</b >

## Original.png
This was our initial proposal, but there were issues when we tried utilising this tech stack for</b >
our extension.

    - Tineye is currently too expensive to implement
    - Scraping fotoforensics was not possible due to bot detection
    - Image metadata extractor APIs did not exist

Our initial assumption that there were API's available for our extension to utilise was wrong</b >
and the team needed to rethink our software design.

## Present.png
This is our current technology stack that we chose to implement.

However producing an ELA image from a upload or link has not been fully implemented, but the draft code</b >
for it is in the repository.

## Future.png
This is proposed future for our extension, utilsing more AWS features such as S3 buckets and AWS rekognition</b >
for outputting ELA on images, sentiment analysis on images, celebrity recognition and metadata extraction.</b >

We wanted to propose this tech stack as it creates less of a dependency on third party services for image</b >
verification. Using these technologies may have also led to the development of a confidence threshold,</b>
where users get a metric on the probability that an image has been digitally manipulated.</b >

Mainly, we saw fit to fully investigate and implement more of AWS as it allows for larger scalability and easier</b >
development down the line.

Not noted in the Future.png SAD but we also thought about extending our services to a web app, making it more</b >
accessible for all, and the possibility of using blockchain technology to create a verified image database.</b >
This could potentially allow for more accurate image verification by comparing images to the blockchain database. 



