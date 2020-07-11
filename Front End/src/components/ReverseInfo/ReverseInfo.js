async function reversedata(input) {
    const imageresult = await GetImageInfo(input);
    let ImageContent = imageresult.related_search_term;
    let numberofResults = imageresult.total_no_results;
    let relatedWords = imageresult.related_key_words;

    // numResults
    // relatedWords

    //Reverse Search Content
    let content = document.getElementById("ImageContent");
    content.innerHTML = (ImageContent + ", " + numberofResults + " results.");

    //Related Words
    let related = document.getElementById("relatedWords");
    for (let i = 0; i < relatedWords.length; i++) {
        let text = relatedWords[i];
        console.log(text);
        let a = document.createElement("li");
        a.href = "#" + text;
        a.textContent = text;
        related.append(a);
    }

    // Related Links
    let RelatedLinks = imageresult.top_urls;
    console.log("Links is ", RelatedLinks);
    let linkDiv = document.getElementById("linklist");

    let listSize = 5;
    for (let i = 0; i < listSize; i++) {
        let text = RelatedLinks[i];
        console.log(text);
        let b = document.createElement("li");
        let a = document.createElement("a");
        a.href = text;
        a.textContent = text;
        a.rel = "noopener noreferrer";
        a.target = "_blank";

        b.append(a);
        // b.onclick = window.open(text);
        linkDiv.append(b);
    }


    // let infoDIV = document.getElementById("imageview");


    return imageresult;
}

async function GetImageInfo(input) {

    let data = {
        "image_url": input
    }

    const url = 'https://lmm2b8jjoe.execute-api.ap-southeast-2.amazonaws.com/image_info';

    const imageData = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .catch(() => console.log("Can’t access " + url + " response. ERROR"))

    return imageData;

}

export default reversedata;

