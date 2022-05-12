import React from 'react'

class ViewFooter extends React.Component {

    constructor(props){
        super(props)
    }

    render(){
        return <div>
            <button>Save to PDF</button>
            <button>Print</button>
        </div>
    }
}

export default ViewFooter;
