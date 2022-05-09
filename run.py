import config as c
import map_xls
import dungeons

# Test various map layouts

# Empty Field
empty_field = dungeons.build_empty_field(15)
map_xls.load_to_xls(empty_field)

# Sparsely Scattered Field
scattered_field = dungeons.build_scattered_field(15)
map_xls.load_to_xls(scattered_field)

# Ruins
ruins = dungeons.build_ruins(15)
map_xls.load_to_xls(ruins)

# Cave Interior (closed)
cave_interior_closed = dungeons.build_cave(15, perimeter_type=c.PERIMETER_CLOSED)
map_xls.load_to_xls(cave_interior_closed)

# Cave Interior (single entry)
cave_interior_single = dungeons.build_cave(15, perimeter_type=c.PERIMETER_SINGLE_ENTRY)
map_xls.load_to_xls(cave_interior_single)

# Cave Interior (dual entry/exit)
cave_interior_dual = dungeons.build_cave(15, perimeter_type=c.PERIMETER_DUAL_ENTRY)
map_xls.load_to_xls(cave_interior_dual)

# Traditional 'Dungeon' (rooms & hallways)
dungeon_room = dungeons.build_dungeon(25)
map_xls.load_to_xls(dungeon_room)
