import React from 'react'

class ViewHeader extends React.Component {

    constructor(props) {
        super(props)
        this.name = 'placeholder_name'
    }

    render(){
        return <div>Your Dungeon: {this.name}</div>
    }
}

export default ViewHeader;