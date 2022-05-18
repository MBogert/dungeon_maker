# Tile Types
WALL = 1
FLOOR = 0

# Coordinate Indexes (y, x)
Y_INDEX = 0
X_INDEX = 1

# Cardinal Directions
NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
DIRECTIONAL_CARDINALS = [NORTH, SOUTH, EAST, WEST]
# Diagonal Cardinals
NORTHWEST = 'NW'
NORTHEAST = 'NE'
SOUTHWEST = 'SW'
SOUTHEAST = 'SE'


# Cardinal Movement (y/x vectors)
CARDINAL_VECTORS = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1),
    NORTHWEST: (-1, -1),
    NORTHEAST: (-1, 1),
    SOUTHWEST: (1, -1),
    SOUTHEAST: (1, 1),
}

# Perimeter Options (currently used in cave templates)
PERIMETER_CLOSED = 'CLOSED'
PERIMETER_SINGLE_ENTRY = 'ONE_ENTRY'
PERIMETER_DUAL_ENTRY = 'TWO_ENTRY'

# File Config Options
LOAD_JSON = ['json']
LOAD_XLSX = ['xlsx']
LOAD_ALL_FILES = LOAD_JSON + LOAD_XLSX