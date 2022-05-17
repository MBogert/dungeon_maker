import React from 'react'
import {ReactComponent as FloorTile } from './img/FloorTile.svg'
import {ReactComponent as WallTile } from './img/WallTile.svg'

class DungeonGrid extends React.Component {

    constructor(props) {
        super(props)
        this.dimension = 10
        this.dungeonMap = createMap(this.dimension)
    }

    render(){
      return (
        <div style={{display:'flex', flexDirection:'column'}}>
          {renderGrid(this.dungeonMap)}
        </div>
      );
    }
}

function renderGrid(gridMap) {
  let gridrows = []
  for(let y=0; y < gridMap.length; y++) {
    let columns = []
    for(let x=0; x < gridMap.length; x++) {
      if(gridMap[y][x] == 0){
        columns.push(<div><FloorTile style={{height:"20px", width:"20px"}}/></div>)
      } else {
        columns.push(<div><WallTile style={{height:"20px", width:"20px"}}/></div>)
      }
    }
    gridrows.push(<div className="gridRow" style={{ display: "flex", flexDirection: "row", justifyContent:'center' }}>{columns}</div>)
  }
  return gridrows
}

function createMap(dimension) {
    let array = new Array(dimension)
    for(let y=0; y < dimension; y++){
        array[y] = new Array(dimension)
    }
    return array
}

export default DungeonGrid;
