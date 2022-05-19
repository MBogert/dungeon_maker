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

# Dungeon room codes
FIELD_EMPTY = 'Field_No_Walls'
FIELD_SCATTERED = 'Field_Some_Walls'
RUINS = 'Ruins'
CAVE_CLOSED = 'Cave_Closed_Walls'
CAVE_SINGLE = 'Cave_Single_Entry'
CAVE_DOUBLE = 'Cave_Dual_Entry'
DUNGEON = 'Dungeon_Inside'
ALL_ROOM_CODES = [FIELD_EMPTY, FIELD_SCATTERED, RUINS, CAVE_CLOSED, CAVE_SINGLE, CAVE_DOUBLE, DUNGEON]

# Miscellaneous I/O code
def print_room_codes():
    print('All Codes        :')
    print('(Open/Closed define whether or not a map\'s perimeter tiles are all Floor or Wall, respectively)')
    print('=================')
    print('Field_No_Walls   : Open dungeon map, all map tiles are floor')
    print('Field_Some_Walls : Open dungeon map, dotted with a handful of small barriers')
    print('Ruins            : Remnants of buildings are scattered throughout an open map')
    print('Cave_Closed_Walls: Enclosed room with a random design of barriers and structures')
    print('Cave_Single_Entry: A closed cave, but with one opening along the perimeter')
    print('Cave_Dual_Entry  : Same as above, but with two openings...')
    print('Dungeon_Inside   : Your traditional run-of-the-mill dungeon, with a collection of rooms and hallways (works best with 20x20 and above)')
    print('=================')
