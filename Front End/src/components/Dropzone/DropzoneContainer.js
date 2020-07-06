import React, { forwardRef } from "react";
import PropTypes from "prop-types";
import { Box } from "grommet";

export const DropzoneContainer = forwardRef(
  ({ children, isDragActive, files, ...rest }, ref) => (
    <Box
      // second white can be changed for box colour
      background={isDragActive || files.length ? "white" : "white"}
      border={{
        color: isDragActive ? "brand" : "light-5",
        style: "dashed",
        size: "small"
      }}
      height={{
        min: "small"
      }}

      align={files.length ? "stretch" : "center"}
      justify="center"
      pad="xsmall"
      ref={ref}
      {...rest}
    >
      {children}
    </Box>
  )
);

DropzoneContainer.propTypes = {
  isDragActive: PropTypes.bool.isRequired,
  files: PropTypes.array.isRequired,
  children: PropTypes.node.isRequired
};
