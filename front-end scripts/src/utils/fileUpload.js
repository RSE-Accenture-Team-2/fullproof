export function fileUpload({ files }) {
  const AWS = require('aws-sdk');

  AWS.config.region = 'ap-southeast-2'; // Region
  AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'ap-southeast-2:c611d523-5be5-4012-8d72-e6fb6cd7b186',
  });

  const uploadImageOnS3 = async (file) => {
    console.log(file)
    const BUCKET_NAME = 'tempimagestorage';
    const IAM_USER_KEY = 'AKIAQBCSCS53TMXTUCFK';
    const IAM_USER_SECRET = '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';

    function uploadToS3(file) {
      let s3bucket = new AWS.S3({
        accessKeyId: IAM_USER_KEY,
        secretAccessKey: IAM_USER_SECRET,
        Bucket: BUCKET_NAME
      });
      s3bucket.createBucket(function () {

        var params = {
          Bucket: BUCKET_NAME,
          Key: file.name,
          Body: file
        };
        s3bucket.upload(params, function (err, data) {
          if (err) {
            console.log('error in callback');
            console.log(err);
          }
          console.log('success');
          console.log(data);
        });
      });
    }

    uploadToS3(file);

  }



  for (let i = 0; i < files.length; i++) {
    uploadImageOnS3(files[i]);
  }

}

