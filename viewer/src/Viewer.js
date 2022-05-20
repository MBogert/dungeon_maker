import React from 'react'
import DungeonGrid from './DungeonGrid'
import ViewFooter from './ViewFooter'

function Viewer(props) {
  const name = props.name
  const grid = props.grid
  const tileSrc = props.tileSrc

  return (
    <div>
      <DungeonGrid grid={grid} name={name} tileSrc={tileSrc}/>
      <ViewFooter />
    </div>
  )
}
export default Viewer;
