function GetImageInfo(input) {

    let data = {
        "image_url": input
    }

    const url = 'https://lmm2b8jjoe.execute-api.ap-southeast-2.amazonaws.com/image_info'; // site that doesn’t send Access-Control-*

    let imageData = fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.text())
        .then(contents => console.log(contents))
        .catch(() => console.log("Can’t access " + url + " response. ERROR"))

    return imageData;
}

export default GetImageInfo;

