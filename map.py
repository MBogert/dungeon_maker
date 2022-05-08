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
            if r.randint(0,100) / 100 < p_mod:
                map_grid[y][x] = c.WALL

def build_wall_clusters(map_grid, p_mod):
    for y in range(0, len(map_grid)):
        for x in range(0, len(map_grid)):
            # Determine if a few tiles will be populated
            if r.randint(0,100) / 100 < p_mod:
                build_cluster(map_grid, y, x)

# Populate a cluster of 2-3 tiles on the map
# Does not check for overlap of existing wall tiles
def build_cluster(map_grid, row, column):
    itr = r.randint(1,3)
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

def build_square_rooms(map_grid):
    room_nums = get_room_count(map_grid)
    coord = (r.randint(0, int(len(map_grid) * 0.05)), r.randint(0, int(len(map_grid) * 0.05)))
    dimension = get_random_valid_dimension(map_grid, coord)
    for itr in list(range(0, room_nums)):
        room_data = build_room(map_grid, coord, dimension)
        coord = get_next_coordinate(map_grid, room_data)
        dimension = get_random_valid_dimension(map_grid, coord)
        build_hallway(map_grid, room_data, (coord, dimension))


# Returns a tuple of room-data on construction
# ( (y_coord, x_coord), room_dimension)
# Expects coord to be (y,x) format
def build_room(map_grid, coord, room_dim):
    for y in range(coord[c.Y_INDEX], coord[c.Y_INDEX] + room_dim):
        for x in range(coord[c.X_INDEX], coord[c.X_INDEX] + room_dim):
            map_grid[y][x] = c.FLOOR
    return (coord, room_dim)

# Assumes room data is tuple format ((y, x), dimension)
# Randomly selects a coordinate from the room's origin point, moving towards the largest sub-quadrant
# Sub-quadrants are divided at room's origin coordinate
def get_next_coordinate(map_grid, room_data):
    zeta = r.randint(0, len(map_grid) - room_data[0][0]) if len(map_grid) - room_data[0][0] > room_data[0][0] else 0
    gamma = r.randint(0, room_data[0][0]) * -1 if room_data[0][0] > len(map_grid) - room_data[0][0] else 0
    upsilon = r.randint(0, len(map_grid) - room_data[0][1]) if len(map_grid) - room_data[0][1] > room_data[0][1] else 0
    omega = r.randint(0, room_data[0][1]) * -1 if room_data[0][1] > len(map_grid) - room_data[0][1] else 0
    return (room_data[0][0] + zeta - gamma, room_data[0][1] + upsilon - omega)


# Coordinate should be the top-left corner of the room, (y, x) format
def get_random_valid_dimension(map_grid, coord):
    return r.randint(3, min(len(map_grid) - coord[0], len(map_grid) - coord[1]))

# Randomly returns a number of rooms that is deemed realistic to populate
def get_room_count(map_grid):
    return r.randint(2, int(len(map_grid) * 0.33))

def build_hallway(map_grid, room_data_1, room_data_2):
    # Randomly calculate hallway data
    hallway = build_hallway_data(room_data_1, room_data_2)
    cardinal = hallway[0]
    width = hallway[2]
    # Use hallway info to populate the map-grid accordingly
    if cardinal is c.NORTH:
        with hallway[1][1] as x_base:
            for y in range(room_data_2[0][0], room_data_1[0][0]):
                for x in range(x_base, x_base + width):
                    map_grid[y][x] = c.FLOOR
    if cardinal is c.SOUTH:
        with hallway[1][1] as x_base:
            for y in range(room_data_1[0][0], room_data_2[0][0]):
                for x in range(x_base, x_base + width):
                    map_grid[y][x] = c.FLOOR
    if cardinal is c.WEST:
        with hallway[1][0] as y_base:
            for y in range(y_base, y_base + width):
                for x in range(room_data_2[0][1], room_data_1[0][1]):
                    map_grid[y][x] = c.FLOOR
    if cardinal is c.EAST:
        with hallway[1][0] as y_base:
            for y in range(y_base, y_base + width):
                for x in range(room_data_1[0][1], room_data_2[0][1]):
                    map_grid[y][x] = c.FLOOR

# Randomly build a tuple of information to build a hallway
# Cardinal direction from room_1 to room_2
# Top/Left-most coordinate of hallway at entrance of room_1
# Width of hallway
def build_hallway_data(room_data_1, room_data_2):
    cardinal = ''
    hallway_coord = (0, 0)
    hall_width = 0

    y_min = min(room_data_1[0][0], room_data_2[0][0])
    x_min = min(room_data_1[0][1], room_data_2[0][1])
    y_max = max(room_data_1[0][0], room_data_2[0][0])
    x_max = max(room_data_1[0][1], room_data_2[0][1])
    width_min = room_data_1[1] if x_min is room_data_1[0][1] else room_data_2[1]
    if y_min is room_data_1[0][0] and x_min + width_min > x_max:
        cardinal = c.NORTH
        if x_min is room_data_1[0][1]:
            hallway_coord = (y_min, room_data_1[0][1] + r.randint(x_min, x_max))
        elif x_min is room_data_2[0][1]:
            hallway_coord = (y_min, room_data_2[0][1] + r.randint(x_min, x_max))
        hall_width = r.randint(1, x_min + width_min - x_max)
    if y_min is room_data_2[0][0] and x_min + width_min > x_max:
        cardinal = c.SOUTH
        if x_min is room_data_1[0][1]:
            hallway_coord = (y_min, room_data_1[0][1] + r.randint(x_min, x_max))
        elif x_min is room_data_2[0][1]:
            hallway_coord = (y_min, room_data_2[0][1] + r.randint(x_min, x_max))
        hall_width = r.randint(1, x_min + width_min - x_max)
    if x_min is room_data_1[0][1] and y_min + width_min > y_max:
        cardinal = c.EAST
        if y_min is room_data_1[0][0]:
            hallway_coord = (room_data_1[0][0] + r.randint(y_min, y_max), x_min)
        elif y_min is room_data_2[0][0]:
            hallway_coord = (room_data_2[0][0] + r.randint(y_min, y_max), x_min)
        hall_width = r.randint(1, y_min + width_min - y_max)
    if x_min is room_data_2[0][1] and y_min + width_min > y_max:
        cardinal = c.WEST
        if y_min is room_data_1[0][0]:
            hallway_coord = (room_data_1[0][0] + r.randint(y_min, y_max), x_min)
        elif y_min is room_data_2[0][0]:
            hallway_coord = (room_data_2[0][0] + r.randint(y_min, y_max), x_min)
        hall_width = r.randint(1, y_min + width_min - y_max)
    return (cardinal, hallway_coord, hall_width)
