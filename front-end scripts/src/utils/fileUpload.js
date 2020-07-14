export function fileUpload({ files }) {

  // console.log(files);
  // const AWS = require('aws-sdk');

  // // Enter copied or downloaded access ID and secret key here
  // const ID = 'AKIAI3SSE4GI4KV6R2HA';
  // const SECRET = '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';

  // // The name of the bucket that you have created
  // const BUCKET_NAME = 'alternate-bucket-reality';

  // const s3 = new AWS.S3({
  //   accessKeyId: ID,
  //   secretAccessKey: SECRET
  // });

  // const params = {
  //   Bucket: BUCKET_NAME,
  //   CreateBucketConfiguration: {
  //     // Set your region here
  //     LocationConstraint: "ap-southeast-2"
  //   }
  // };

  // s3.createBucket(params, function (err, data) {
  //   if (err) console.log(err, err.stack);
  //   else console.log('Bucket Created Successfully', data.Location);
  // });

  var formData = new FormData();

  for (let i = 0; i < files.length; i++) {
    formData.append(files[i].name, files[i]);
    console.log(files[i]);
  }

  // console.log(formData);

  // // var base64data = new Buffer(formData, 'binary');


  // function upload(f) {

  //   // Setting up S3 upload parameters
  //   const params = {
  //     Bucket: BUCKET_NAME,
  //     Key: 'data.jpg', // File name you want to save as in S3
  //     Body: f
  //   };

  //   // Uploading files to the bucket
  //   s3.upload(params, function (err, data) {
  //     if (err) {
  //       throw err;
  //     }
  //     console.log(`File uploaded successfully. ${data.Location}`);
  //   });

  // }

  // upload(files[0]);









  // console.log(formData);

  // return fetch("https://my-website.com/api/file/upload", {
  //   method: "POST",
  //   // if your app is storing auth tokens in a cookie include credentials
  //   // credentials: 'include',
  //   body: formData
  // })
  //   .then(response =>
  //     response.json().then(json => ({
  //       status: response.status,
  //       statusText: response.statusText,
  //       json
  //     }))
  //   )
  //   .then(({ status, statusText, json }) => {
  //     if (status >= 400) {
  //       // API returned a crappy response
  //       console.log("error:", status, statusText, json);
  //     } else {
  //       // Upload done!
  //       return json;
  //     }
  //   })
  //   .catch(err => console.log(err));
}
