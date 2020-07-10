import React from "react";
import ReactDOM from "react-dom";
import { Toggle } from "react-toggle-component";
import './index.scss';
import { Grommet } from "grommet";
import { MyForm } from "./components";

class Logo extends React.Component {
  render() {
    return (

      <div className="size" >
        <img className="Logo" src="./logo_large.png" alt=""></img>
      </div>
    );
  }
}

class DropForm extends React.Component {
  render() {
    return (
      <Grommet>
        <MyForm />
      </Grommet>
    );
  }
}





class App extends React.Component {
  render() {





    return (
      <div className="appcontent">
        <div className="block">
          <Logo />
          <br></br>
          Drag and drop an image to verify its authenticity.
          </div>
        <hr />

        <div className="block">
          <div className="flex-spacer">
            <p>Reverse Image Search</p>
            <Toggle
              leftBackgroundColor="#D1D1D1"
              rightBackgroundColor="#663399"
              borderColor="none"
              knobColor="white"
              name="toggle-1"
              onToggle={e => console.log("onToggle1", e.target.checked)}
            />
          </div>
          <hr />
        </div>

        <div className="block">
          <div className="flex-spacer">
            <p>Check digital image manipulation</p>
            <Toggle
              leftBackgroundColor="#D1D1D1"
              rightBackgroundColor="#663399"
              borderColor="none"
              knobColor="white"
              name="toggle-2"
              onToggle={e => console.log("onToggle2", e.target.checked)}
            />
            {/* window.location.href */}
          </div>
          <hr />
        </div>

        <div className="block">
          <div className="flex-spacer">
            <p>Show in feed</p>
            <Toggle
              leftBackgroundColor="#D1D1D1"
              rightBackgroundColor="#663399"
              borderColor="none"
              knobColor="white"
              name="toggle-3"
              onToggle={e => console.log("onToggle3", e.target.checked)}
            />
          </div>
        </div>

        <div className="block dropper">
          <DropForm />
        </div>

        {/* <div>
          <Getlinks link={link} />
        </div> */}
        <hr />

        <div id="imageview" className="block italic">
          {/* // let ImageContent = imageresult.related_search_term;
    // let RelatedLinks = imageresult.top_urls;
    // let numberofResults = imageresult.total_no_results;
    // let relatedWords = imageresult.related_key_words; */}

          <h2>Reverse Search</h2>
          <hr></hr>
          <h3 id="ImageContent">Image</h3>
          <hr></hr>
          <h3>Related Words</h3>
          <ul id="relatedWords"> </ul>
          <hr></hr>
          <h3>Related Links</h3>
          <hr></hr>
          <ul id="linklist"></ul>
        </div>


        <div id="imageview" className="block italic">
          <h2>Meta Data</h2>
          <hr></hr>

        </div>



      </div>
    );
  }
}

export default App;


const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
