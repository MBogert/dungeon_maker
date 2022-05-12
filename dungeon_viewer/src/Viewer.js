import React from 'react'
import ViewHeader from './ViewHeader'
import DungeonGrid from './DungeonGrid'
import ViewFooter from './ViewFooter'

class Viewer extends React.Component {

    constructor(props){
        super(props)
    }

    render(){
        return <div>
            <ViewHeader/>
            <DungeonGrid/>
            <ViewFooter/>
        </div>
    }
}

export default Viewer;