import React from 'react';

class Getlinks extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: "no link yet"
        }
    }

    render() {
        let input = this.state.value;

        function fetchlinks() {

            let data = {
                "url": input
            }

            const url = 'https://lmm2b8jjoe.execute-api.ap-southeast-2.amazonaws.com/scrape'; // site that doesn’t send Access-Control-*

            fetch(url, {
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json"
                }
            })
                .then(response => response.text())
                .then(contents => console.log(contents))
                .catch(() => console.log("Can’t access " + url + " response. ERROR"))
        }

        fetchlinks()
        return (1);
    }
}

export default Getlinks;