import config as c
from load_map import load_dungeon_to_file
import dungeons
from render_dungeon import startup_webapp

# Empty Field
empty_field = dungeons.build_empty_field(15)
load_dungeon_to_file(empty_field)

# Sparsely Scattered Field
scattered_field = dungeons.build_scattered_field(15)
load_dungeon_to_file(scattered_field)

# Ruins
ruins = dungeons.build_ruins(15)
load_dungeon_to_file(ruins)

# Cave Interior (closed)
cave_interior_closed = dungeons.build_cave(15, perimeter_type=c.PERIMETER_CLOSED)
load_dungeon_to_file(cave_interior_closed)

# Cave Interior (single entry)
cave_interior_single = dungeons.build_cave(15, perimeter_type=c.PERIMETER_SINGLE_ENTRY)
load_dungeon_to_file(cave_interior_single)

# Cave Interior (dual entry/exit)
cave_interior_dual = dungeons.build_cave(15, perimeter_type=c.PERIMETER_DUAL_ENTRY)
load_dungeon_to_file(cave_interior_dual)

# Traditional 'Dungeon' (rooms & hallways)
dungeon_room = dungeons.build_dungeon(25)
load_dungeon_to_file(dungeon_room)

# Run the React Node project and load an example data structure to render
# TODO
startup_webapp()