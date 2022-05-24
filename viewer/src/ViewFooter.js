import React from 'react'
import ViewerButton from './ViewerButton';

export const footerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'center',
}

function ViewFooter(){

    return(<div style={footerStyle} className="nonprintable">
            <ViewerButton name={'Save'} onClickFn={() => console.log('TODO: Implement save')}/>
            <ViewerButton name={'Print/PDF'} onClickFn={() => window.print()}/>
            <ViewerButton name={'Quit'} onClickFn={() => window.close()}/>
          </div>
        )
}

export default ViewFooter;
