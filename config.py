# Tile Types
WALL = 1
FLOOR = 0

DUNGEON_FILE_DEFAULT = 'dungeon.xlsx'
DUNGEON_DIRECTORY = 'dungeons/'

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
DIAGONAL_CARDINALS = [NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST]
#
ALL_CARDINALS = DIRECTIONAL_CARDINALS + DIAGONAL_CARDINALS

Y_INDEX = 0
X_INDEX = 1

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

# Perimeter Options
PERIMETER_CLOSED = 'CLOSED'
PERIMETER_SINGLE_ENTRY = 'ONE_ENTRY'
PERIMETER_DUAL_ENTRY = 'TWO_ENTRY'