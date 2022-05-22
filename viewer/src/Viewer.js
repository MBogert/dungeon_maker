import React from 'react'
import DungeonGrid from './DungeonGrid'
import ViewFooter from './ViewFooter'
import ViewHeader from './ViewHeader'

function Viewer(props) {
  const name = props.name
  const grid = props.grid

  return (
    <div>
      <ViewHeader name={name}/>
      <DungeonGrid grid={grid} name={name}/>
      <ViewFooter />
    </div>
  )
}

export default Viewer;
