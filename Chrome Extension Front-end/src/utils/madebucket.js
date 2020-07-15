// export function fileUpload({ files }) {
//   const AWS = require('aws-sdk');

//   AWS.config.region = 'ap-southeast-2'; // Region
//   AWS.config.credentials = new AWS.CognitoIdentityCredentials({
//     IdentityPoolId: 'ap-southeast-2:c611d523-5be5-4012-8d72-e6fb6cd7b186',
//   });

const AWS = require('aws-sdk');
// Enter copied or downloaded access ID and secret key here
const ID = 'AKIAI3SSE4GI4KV6R2HA';
const SECRET = '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';

// The name of the bucket that you have created
const BUCKET_NAME = 'alternate-bucket-reality';

const s3 = new AWS.S3({
    accessKeyId: ID,
    secretAccessKey: SECRET
});

const params = {
    Bucket: BUCKET_NAME,
    CreateBucketConfiguration: {
        // Set your region here
        LocationConstraint: "ap-southeast-2"
    }
};

s3.createBucket(params, function (err, data) {
    if (err) console.log(err, err.stack);
    else console.log('Bucket Created Successfully', data.Location);
});

  // for (let i = 0; i < files.length; i++) {
  //   uploadImageOnS3(files[i]);
  // }

// }

