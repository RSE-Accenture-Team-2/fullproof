export function fileUpload({ firstName, lastName, files }) {
  let formData = new FormData();

  files.forEach(name => {
    formData.append(name, files[name]);
  });
  formData.append(firstName, firstName);
  formData.append(lastName, lastName);

  return fetch("https://lmm2b8jjoe.execute-api.ap-southeast-2.amazonaws.com/sendForm", {
    method: "POST",
    body: formData
  })
    .then(response =>
      response.json().then(json => ({
        status: response.status,
        statusText: response.statusText,
        json
      }))
    )
    .then(({ status, statusText, json }) => {
      if (status >= 400) {
        // API returned a crappy response
        console.log("error:", status, statusText, json);
      } else {
        // Upload done!
        return json;
      }
    })
    .catch(err => console.log(err));
}
