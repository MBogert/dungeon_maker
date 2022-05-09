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


# Randomly populate wall tiles across an empty dungeon floor
def populate_wall_tiles(map_grid, p_mod):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            # Determine if wall tile will be populated
            if r.randint(0, 100) / 100 < p_mod:
                map_grid[y][x] = c.WALL


def build_wall_clusters(map_grid, p_mod):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            # Determine if a few tiles will be populated
            if r.randint(0, 100) / 100 < p_mod:
                build_cluster(map_grid, y, x)


# Populate a cluster of 2-3 tiles on the map
# Does not check for overlap of existing wall tiles
def build_cluster(map_grid, row, column):
    itr = r.randint(1, 3)
    while itr > 0:
        map_grid[row][column] = c.WALL
        next_direction = r.choice(get_valid_cardinals(map_grid, row, column, False))
        row += c.CARDINAL_VECTORS[next_direction][c.Y_INDEX]
        column += c.CARDINAL_VECTORS[next_direction][c.X_INDEX]
        itr -= 1


# Returns a subset of cardinal directions which you could move from a given tile on a map
# 'diaganol' is a flag for whether or not to consider diaganol adjacency
def get_valid_cardinals(map_grid, row, column, diaganol):
    valid_cardinals = []
    if row > 0:
        valid_cardinals.append(c.NORTH)
    if column > 0:
        valid_cardinals.append(c.WEST)
    if row < len(map_grid) - 1:
        valid_cardinals.append(c.SOUTH)
    if column < len(map_grid) - 1:
        valid_cardinals.append(c.EAST)
    if diaganol:
        if row > 0 and column > 0:
            valid_cardinals.append(c.NORTHWEST)
        if row > 0 and column < len(map_grid) - 1:
            valid_cardinals.append(c.NORTHEAST)
        if row < len(map_grid) - 1 and column > 0:
            valid_cardinals.append(c.SOUTHWEST)
        if row < len(map_grid) - 1 and column < len(map_grid) - 1:
            valid_cardinals.append(c.SOUTHEAST)
    return valid_cardinals


# Clears all tiles of a given type, which have no adjacent matching tiles
# Default clear state is a FLOOR tile
# This considers diagonal adjacency
def remove_adjacentless_tiles(map_grid, tile_type):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            if map_grid[y][x] == tile_type and has_adjacent_tile(map_grid, y, x) is not True:
                map_grid[y][x] = c.FLOOR


def has_adjacent_tile(map_grid, y, x):
    tile_type = map_grid[y][x]
    cardinals = get_valid_cardinals(map_grid, y, x, True)
    for cardinal in cardinals:
        y_adj = y + c.CARDINAL_VECTORS[cardinal][c.Y_INDEX]
        x_adj = x + c.CARDINAL_VECTORS[cardinal][c.X_INDEX]
        if map_grid[y_adj][x_adj] == tile_type:
            return True
    return False


# || Methods for manipulating the perimeter grid of a map || #
def closed_perimeter(map_grid):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            if y == 0 or x == 0 or y == len(map_grid) - 1 or x == len(map_grid) - 1:
                map_grid[y][x] = c.WALL


def single_entry_perimeter(map_grid):
    closed_perimeter(map_grid)
    # Select a random wall to place an entry-point
    cardinal_entry = r.choice(c.DIRECTIONAL_CARDINALS)
    build_perimeter_entrance(map_grid, cardinal_entry)


def dual_entry_perimeter(map_grid):
    closed_perimeter(map_grid)
    # Select two random walls to place entry-points
    cardinal_entry_one = r.choice(c.DIRECTIONAL_CARDINALS)
    cardinal_entry_two = r.choice(list(set(c.DIRECTIONAL_CARDINALS) - set(cardinal_entry_one)))
    build_perimeter_entrance(map_grid, cardinal_entry_one)
    build_perimeter_entrance(map_grid, cardinal_entry_two)


def build_perimeter_entrance(map_grid, cardinal):
    entry_width = int(len(map_grid) * 0.20)
    entry_index = r.randint(0, len(map_grid) - entry_width)
    if cardinal is c.NORTH:
        for perim_tile in range(entry_index, entry_index + entry_width):
            map_grid[0][perim_tile] = c.FLOOR
    elif cardinal is c.SOUTH:
        for perim_tile in range(entry_index, entry_index + entry_width):
            map_grid[len(map_grid) - 1][perim_tile] = c.FLOOR
    elif cardinal is c.EAST:
        for perim_tile in range(entry_index, entry_index + entry_width):
            map_grid[perim_tile][len(map_grid) - 1] = c.FLOOR
    elif cardinal is c.WEST:
        for perim_tile in range(entry_index, entry_index + entry_width):
            map_grid[perim_tile][0] = c.FLOOR


build_perimeter = {
    c.PERIMETER_CLOSED: closed_perimeter,
    c.PERIMETER_SINGLE_ENTRY: single_entry_perimeter,
    c.PERIMETER_DUAL_ENTRY: dual_entry_perimeter,
}


# || ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== || #

def populate_square_dungeon(dungeon):
    # Randomly select a coordinate on the top left quadrant
    x = r.randint(0, int(len(dungeon) * 0.50))
    y = r.randint(0, int(len(dungeon) * 0.50))
    length = r.randint(1, int(len(dungeon) * 0.25))
    # Create a given number of rooms, directly proportional to dungeon size
    for counter in range(int(len(dungeon) * 0.25)):
        # Populate the square room with given (y, x) and length
        for i in range(y, y + length):
            for j in range(x, x + length):
                dungeon[i][j] = c.FLOOR
        prev_x = x
        prev_y = y
        # Randomly select a new (y, x) and length for the next room
        x = r.randint(0, len(dungeon) - 2)
        y = r.randint(0, len(dungeon) - 2)
        length = r.randint(1, min(len(dungeon) - y, len(dungeon) - x))
        # Connect rooms via halls
        for i in range(min(x, prev_x), max(x, prev_x)):
            dungeon[y][i] = c.FLOOR
        for i in range(min(y, prev_y), max(y, prev_y)):
            dungeon[i][x] = c.FLOOR
    return dungeon
