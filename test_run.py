# To test different builds

import config as c
from load_map import load_dungeon_to_file
import dungeons
from render_dungeon import startup_webapp

# Empty Field
empty_field = dungeons.dungeon_builds[c.FIELD_EMPTY](15)
load_dungeon_to_file(empty_field)

# Sparsely Scattered Field
scattered_field = dungeons.dungeon_builds[c.FIELD_SCATTERED](15)
load_dungeon_to_file(scattered_field)

# Ruins
ruins = dungeons.dungeon_builds[c.RUINS](15)
load_dungeon_to_file(ruins)

# Cave Interior (closed)
cave_interior_closed = dungeons.dungeon_builds[c.CAVE_CLOSED](15)
load_dungeon_to_file(cave_interior_closed)

# Cave Interior (single entry)
cave_interior_single = dungeons.dungeon_builds[c.CAVE_SINGLE](15)
load_dungeon_to_file(cave_interior_single)

# Cave Interior (dual entry/exit)
cave_interior_dual = dungeons.dungeon_builds[c.CAVE_DOUBLE](15)
load_dungeon_to_file(cave_interior_dual)

# Traditional 'Dungeon' (rooms & hallways)
dungeon_room = dungeons.dungeon_builds[c.DUNGEON](25)
load_dungeon_to_file(dungeon_room)

# Run the React Node project and load an example data structure to render
# TODO
startup_webapp()