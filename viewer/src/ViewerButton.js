import React from 'react'

const btnStyle = {
  padding: '0px 10px'
}

function ViewerButton(props) {

  const name = props.name

  return (<div style={btnStyle}>
      <button>{name}</button>
    </div>
  )
}

export default ViewerButton;
