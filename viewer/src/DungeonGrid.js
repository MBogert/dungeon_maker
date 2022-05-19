import React from 'react'
import {ReactComponent as WallTile } from './img/floor_tile.svg'
import {ReactComponent as FloorTile } from './img/wall_tile.svg'

const gridStyle = {
  display: 'inline-block',
  border: 'dashed',
  borderWidth: 'medium'
}

function DungeonGrid(props) {
  const dungeon_grid = props.dungeon_grid
  return (
    <div style={gridStyle}>
      {renderGrid(dungeon_grid)}
    </div>
  )
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

export default DungeonGrid;
