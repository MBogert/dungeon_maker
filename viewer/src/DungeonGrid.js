import React, {useState} from 'react'
import findDOMNode from 'react-dom'
import {ReactComponent as WallTile } from './img/floor_tile.svg'
import {ReactComponent as FloorTile } from './img/wall_tile.svg'

export const headerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
}

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

const braveKinght = 'https://i1.sndcdn.com/artworks-000479173020-7mj3zz-t500x500.jpg'
const potionSeller = 'https://static.miraheze.org/thefinalrumblewiki/8/84/Potion_seller.png'

function DungeonGrid(props) {
  const [name, setName] = useState(props.name)
  const [tileSrc, setTileSrc] = useState(props.tileSrc)
  const [grid, setGrid] = useState(props.grid)

  return (<div>
    <div style={headerStyle}>
       <div></div>
       <h1 contentEditable={true} onChange={() => setName(findDOMNode(this).innerText)}>{name}</h1>
       <div style={tileStyle}>
         <h1>Tile:</h1>
         <img style={imgStyleWall} src={tileSrc} onClick={() => setTileSrc(tileSrc === potionSeller ? braveKinght : potionSeller)} alt='Potion Seller! I request your FINEST potions!'/>
       </div>
     </div>
    <div style={gridStyle}>
      {renderGrid(grid)}
    </div>
  </div>
  )
}

function renderGrid(gridMap) {
  let gridrows = []
  for(let y=0; y < gridMap.length; y++) {
    let columns = []
    for(let x=0; x < gridMap.length; x++) {
      if(gridMap[y][x] === 0){
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
