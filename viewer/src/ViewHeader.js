import React from 'react'

const headerStyle = {
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
}

const imgStyleWall = {
  width: '50px',
  height: '50px',
  display: 'inline',
}

const imgStyleTile = {
  width: '50px',
  height: '50px',
  display: 'none',
}

const tileStyle = {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'flex-start',
}

function ViewHeader(props) {
  const dungeon_name = props.dungeon_name
  const current_tile = props.current_tile

  return <div style={headerStyle}>
      <div></div>
      <h1>{dungeon_name}</h1>
      <div style={tileStyle}>
        <p>Tile: {current_tile}</p>
        <img style={imgStyleTile} src='https://i1.sndcdn.com/artworks-000479173020-7mj3zz-t500x500.jpg'/>
        <img style={imgStyleWall} src='https://static.miraheze.org/thefinalrumblewiki/8/84/Potion_seller.png'/>
      </div>
    </div>
}

export default ViewHeader;
