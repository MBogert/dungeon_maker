import React from 'react'
import ViewHeader from './ViewHeader'
import DungeonGrid from './DungeonGrid'
import ViewFooter from './ViewFooter'

function Viewer(props) {
  const dungeon_name = props.dungeon_name
  const dungeon_grid = props.dungeon_grid
  const current_tile = props.current_tile

  return (
    <div>
      <ViewHeader dungeon_name={dungeon_name} current_tile={current_tile}/>
      <DungeonGrid dungeon_grid={dungeon_grid} />
      <ViewFooter />
    </div>
  )
}
export default Viewer;
