# fullproof: The Development of the Software
These are all of our Software Architecture Diagrams that were made during our project.</b >

## Original.png
This was our initial proposal, but there were issues when we tried utilising this tech stack for</b >
our extension.

    - Tineye is currently too expensive to implement
    - Scraping fotoforensics was not possible due to bot detection
    - ELA APIs do not exist

Our initial assumption that there were API's available for our extension to utilise was wrong</b >
and the team needed to rethink our software design.

## MVP.png
This is proposed future for our extension, utilsing AWS S3 buckets to automatically trigger lambdas and AWS rekognition</b >
for outputting ELA on images, sentiment analysis on images, celebrity recognition and metadata extraction.</b >

We wanted to propose this tech stack as it creates less of a dependency on third party services for image</b >
verification. Using these technologies may have also led to the development of a confidence threshold,</b>
where users get a metric on the probability that an image has been digitally manipulated.</b >

Producing an ELA image from a upload or link has not been fully implemented, but the draft code</b >
for it is in the repository.

Mainly, we saw fit to fully investigate and implement more of AWS as it allows for larger scalability and easier</b >
development down the line.

