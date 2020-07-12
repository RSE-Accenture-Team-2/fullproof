import React, { useState } from "react";
import { Box, Button, Form, FormField, ThemeContext } from "grommet";
import { Dropzone } from "./Dropzone";
import { fileUpload } from "../utils";
import reversedata from "../components/ReverseInfo/ReverseInfo.js";

export const MyForm = () => {
  const [files, setFiles] = useState([]);
  // The addFiles and deleteFiles functions ensure that the files that will be
  // submitted by the form stay aligned with the files present in the dropzone.
  // Be sure to include these functions with the onAddFiles and onDeleteFiles
  // props of the Dropzone if you intend to use file uploading.
  const addFiles = newFiles => {
    setFiles(...files, newFiles);
  };

  const deleteFiles = remainingFiles => {
    setFiles(remainingFiles);
  };



  const handleSubmit = event => {
    event.preventDefault();

    let formlink = document.getElementById("LinkURL").value;
    if (formlink !== '') {
      document.getElementById("imagecontent").style.display = "block";
      reversedata(formlink);
    }
    // You will need to update ../utils/fileUpload with the correct url for
    // where the data will be sent to.
    fileUpload({ files });


  };

  return (
    <Box
      // box width
      width="290px"
      gap="0"
      onDrop={event => event.preventDefault()} // Prevent document drop from overtaking window
    >
      <Form onSubmit={handleSubmit}>
        <ThemeContext.Extend
          value={{
            formField: {
              border: {
                color: "none"
              },
              label: {
                margin: {
                  bottom: "small"
                }
              },
              margin: {
                bottom: "medium"
              }
            }
          }}
        >
          <FormField>
            {/* In order to utilize fileUpload, you need to provide
             * the onAddFiles and onDeleteFiles props and their associated functions
             */}
            <input type='url' id="LinkURL" className='URL' placeholder='URL'></input>
            <hr></hr>
            <Dropzone
              multiple
              showPreview
              showFileSize
              onAddFiles={addFiles}
              onDeleteFiles={deleteFiles}
            />
          </FormField>
        </ThemeContext.Extend>
        <Box align="start" direction="row" gap="xsmall">
          <Button type="submit" label="Submit" primary />
        </Box>
      </Form>
    </Box>
  );
};
