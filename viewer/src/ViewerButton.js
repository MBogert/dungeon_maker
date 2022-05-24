import React from 'react'

const btnStyle = {
  padding: '0px 10px'
}

function ViewerButton(props) {

  const name = props.name
  const onClickFn = props.onClickFn

  return (<div style={btnStyle}>
      <button onClick={onClickFn}>{name}</button>
    </div>
  )
}

export default ViewerButton;
