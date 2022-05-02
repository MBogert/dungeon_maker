import map
import config as c
import random as r

# Return maps with different layouts, without having to understand specific map operations

def build_empty_field(dim):
    return map.init_empty_map(dimension=dim, default_tile=c.FLOOR)

def build_scattered_field(dim):
    dungeon = map.init_empty_map(dimension=dim, default_tile=c.FLOOR)
    map.build_wall_clusters(map_grid=dungeon, p_mod=0.02)
    return dungeon

def build_ruins(dim):
    return map.build_dungeon_map(dimension=dim, p_mod=0.15)