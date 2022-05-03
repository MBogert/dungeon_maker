DIMENSION_MAX = 50
DIMENSION_MIN = 10
DIMENSION_DEFAULT = 25

ROOM_COUNT_DEFAULT = 5
ROOM_DIMENSION_DEFAULT = 10
ROOM_DIMENSION_MIN = 4

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
# Diaganol Cardinals
NORTHWEST = 'NW'
NORTHEAST = 'NE'
SOUTHWEST = 'SW'
SOUTHEAST = 'SE'
CARDINALS = ['N', 'S', 'E', 'W','NW', 'NE', 'SW', 'SE']

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
