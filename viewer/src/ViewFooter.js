import React from 'react'



export const footerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-around',
}

function ViewFooter(){

    return(<div style={footerStyle}>
            <button>Save</button>
            <button>PDF</button>
            <button>Quit</button>
          </div>
        )
}

export default ViewFooter;
