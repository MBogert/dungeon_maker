import React from 'react'
import Uploady from "@rpldy/uploady"
import UploadButton from "@rpldy/upload-button";

class ViewFooter extends React.Component {

  constructor(props) {
    super(props)
  }

  render() {
    return <Uploady>
        <UploadButton/>
      </Uploady>

  }
}

export default ViewFooter;
