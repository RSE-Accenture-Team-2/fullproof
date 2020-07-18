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
This is the final software architecture we built our prototype for. It cleverly uses the AWS SDK and S3 to </b >
automatically trigger lambdas and AWS rekognition for outputting ELA on images, celebrity recognition and metadata </b >
extraction.</b >

We wanted to propose this tech stack as it creates less of a dependency on third party services for image 
verification and this architecture is highly scalable.</b >

Producing an ELA image from a upload or link has not been fully implemented, but the draft code</b >
for it is in the repository.

Mainly, we saw fit to fully investigate and implement more of AWS as it allows for larger scalability and easier</b >
development down the line.

