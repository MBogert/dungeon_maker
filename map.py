import config as c
import random as r

def print_map(map_grid):
    print("= " * (len(map_grid) + 2))
    for row in map_grid:
        print("||", end='')
        print(*row, sep=" ", end='')
        print("||")
    print("= " * (len(map_grid) + 2))

# Builds map with all of one type of tile
# Should be WALL or FLOOR
def init_empty_map(dimension, default_tile):
    map_grid = []
    for i in range(dimension):
        map_grid.append([default_tile] * dimension)
    return map_grid

def build_dungeon_map(dimension, p_mod):
    map_grid = init_empty_map(dimension, c.FLOOR)
    build_dungeon_walls(map_grid, p_mod)
    return map_grid

# Randomly populate clusters of walls across an empty dungeon floor
# Leverages percent-modifier for odds of wall population
def build_dungeon_walls(map_grid, p_mod):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            # Determine if wall tile will be populated
            if r.randint(0,100) / 100 < p_mod:
                map_grid[y][x] = c.WALL

def build_wall_clusters(map_grid, p_mod):
    for y in range(0, len(map_grid) - 1):
        for x in range(0, len(map_grid) - 1):
            # Determine if a few tiles will be populated
            if r.randint(0,100) / 100 < p_mod:
                build_cluster(map_grid, y, x)

# Populate a cluster of 2-3 tiles on the map
# Does not check for overlap of existing wall tiles
def build_cluster(map_grid, row, column):
    itr = r.randint(1,3)
    while itr > 0:
        map_grid[row][column] = c.WALL
        next_dir = r.choice(get_valid_directions(map_grid, row, column))
        row += c.CARDINAL_VECTORS[next_dir][c.ROW_INDEX]
        column += c.CARDINAL_VECTORS[next_dir][c.COL_INDEX]
        itr -= 1

# Returns a subset of cardinal directions which you could move from a given tile on a map
def get_valid_directions(map_grid, row, column):
    valid_cardinals = []
    if row > 0:
        valid_cardinals.append(c.NORTH)
    if column > 0:
        valid_cardinals.append(c.WEST)
    if row < len(map_grid) - 1:
        valid_cardinals.append(c.SOUTH)
    if column < len(map_grid) - 1:
        valid_cardinals.append(c.EAST)
    return valid_cardinals

