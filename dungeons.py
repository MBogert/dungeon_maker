import map
import config as c


# Return maps with different layouts, without having to understand specific map operations

def build_empty_field(dim):
    return map.init_empty_map(dimension=dim, default_tile=c.FLOOR)


def build_scattered_field(dim):
    dungeon = map.init_empty_map(dimension=dim, default_tile=c.FLOOR)
    map.build_wall_clusters(map_grid=dungeon, p_mod=0.03)
    return dungeon

# TODO enhance
def build_ruins(dim):
    dungeon = map.init_empty_map(dimension=dim, default_tile=c.FLOOR)
    map.populate_wall_tiles(map_grid=dungeon, p_mod=0.15)
    map.remove_adjacentless_tiles(map_grid=dungeon, tile_type=c.WALL)
    return dungeon

def build_closed_cave(dim):
    return build_cave(dim, c.PERIMETER_CLOSED)

def build_single_entry_cave(dim):
    return build_cave(dim, c.PERIMETER_SINGLE_ENTRY)

def build_dual_entry_cave(dim):
    return build_cave(dim, c.PERIMETER_DUAL_ENTRY)

# Different Options
# PERIMETER_CLOSED (closed cave)
# PERIMETER_SINGLE_ENTRY (cave with one entrance)
# PERIMETER_DUAL_ENTRY (cave with two entrances)
def build_cave(dim, perimeter_type):
    dungeon = map.init_empty_map(dimension=dim, default_tile=c.FLOOR)
    map.build_wall_clusters(map_grid=dungeon, p_mod=0.08)
    map.build_perimeter[perimeter_type](map_grid=dungeon)
    return dungeon


# Works best w/ dimensions 20x20 and above
# TODO Enhance
def build_dungeon(dim):
    dungeon = map.init_empty_map(dimension=dim, default_tile=c.WALL)
    map.populate_square_dungeon(dungeon)
    return dungeon

# Use the below to access any build methods
dungeon_builds = {
    c.FIELD_EMPTY: build_empty_field,
    c.FIELD_SCATTERED: build_scattered_field,
    c.RUINS: build_ruins,
    c.CAVE_CLOSED: build_closed_cave,
    c.CAVE_SINGLE: build_single_entry_cave,
    c.CAVE_DOUBLE: build_dual_entry_cave,
    c.DUNGEON: build_dungeon
}