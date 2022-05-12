import React from 'react'
import { Card } from "@rneui/themed";

class DungeonGrid extends React.Component {
    constructor(props) {
        super(props)
        this.dimension = 5
        this.dungeonMap = createMap(this.dimension)
    }

    render(){
        var dungeonTiles = this.dungeonMap.map(function(){
        return
        <Card containerStyle={{ marginTop: 15 }}>
          <Card.Title>Tile</Card.Title>
        </Card>;})
        return <div>HALLLO I AM THE GRID </div>
    }
}

function createMap(dimension) {
    let array = new Array(dimension)
    for(let i=0; i < dimension; i++){
        array[i] = new Array(dimension)
    }
    return array
}

export default DungeonGrid;