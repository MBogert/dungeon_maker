import React from 'react'
import ViewerButton from './ViewerButton';

export const footerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
}

function ViewFooter(){

    return(<div style={footerStyle}>
            <ViewerButton name={'Save'} />
            <ViewerButton name={'PDF'} />
            <ViewerButton name={'Quit'} />
          </div>
        )
}

export default ViewFooter;
