import map_xls
import dungeons

# Test various map layouts

# Empty Field
empty_field = dungeons.build_empty_field(15)
map_xls.load_to_xls(empty_field)

# Sparsely Scattered Field
scattered_1 = dungeons.build_scattered_field(15)
map_xls.load_to_xls(scattered_1)

# Ruins
ruins = dungeons.build_ruins(15)
map_xls.load_to_xls(ruins)

# Cave Interior
cave = dungeons.build_cave(15)
map_xls.load_to_xls(cave)
