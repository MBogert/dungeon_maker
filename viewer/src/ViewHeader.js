import React, {useState} from 'react'
import findDOMNode from 'react-dom'

const headerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
}

function ViewHeader(props) {

  const [name, setName] = useState(props.name)

  return (<div style={headerStyle} className="nonprintable">
     <h1 contentEditable={true} onChange={() => setName(findDOMNode(this).innerText)}>{name}</h1>
   </div>)
}

export default ViewHeader;
