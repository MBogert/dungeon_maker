import React from 'react'
import {ReactComponent as WallTile } from './img/floor_tile.svg'
import {ReactComponent as FloorTile } from './img/wall_tile.svg'

export const imgStyleWall = {
  width: '50px',
  height: '50px',
  display: 'inline',
}

export const imgStyleTile = {
  width: '50px',
  height: '50px',
  display: 'none',
}

export const tileStyle = {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'flex-start',
}

const gridStyle = {
  display: 'inline-block',
  border: 'dashed',
  borderWidth: 'medium',
}

class DungeonGridClass extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      grid: props.grid,
    }
  }

  setGrid(y, x, value) {
    let newGrid = this.state.grid
    newGrid[y][x] = value
    return this.state.grid
  }

  renderGrid(gridMap) {
    let gridrows = []
    for(let y=0; y < gridMap.length; y++) {
      let columns = []
      for(let x=0; x < gridMap.length; x++) {
        if(gridMap[y][x] === 0){
          columns.push(<div onClick={() => this.setState({grid: this.setGrid(y, x, 1)})}><FloorTile style={{height:"20px", width:"20px"}}/></div>)
        } else {
          columns.push(<div onClick={() => this.setState({grid: this.setGrid(y, x, 0)})}><WallTile style={{height:"20px", width:"20px"}}/></div>)
        }
      }
      gridrows.push(<div className="gridRow" style={{ display: "flex", flexDirection: "row", justifyContent:'center' }}>{columns}</div>)
    }
    return gridrows
  }

  render() {
      return <div style={gridStyle}>
        {this.renderGrid(this.state.grid)}
      </div>
  }
}

export default DungeonGridClass;
