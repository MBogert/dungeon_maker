# Code to move/delete

import config as c
import random
import xlsxwriter

def create_square_dungeon(dimension):
    dungeon = []
    for i in range(dimension):
        dungeon.append([c.WALL] * dimension)
    return dungeon

def print_dungeon(dungeon):
    print("= " * (len(dungeon) + 2))
    for row in dungeon:
        print("||", end='')
        print(*row, sep=" ", end='')
        print("||")
    print("= " * (len(dungeon) + 2))

def print_dungeon_tiles(dungeon):
    print("Your Dungeon:")
    print("=" * (len(dungeon)* 3))
    for i in range(len(dungeon)):
        for itr in range(3):
            for j in range(len(dungeon)):
                if itr == 1:
                    if dungeon[i][j] == c.FLOOR:
                        print("***", end='')
                    else:
                        print("|=|", end='')
                else: # Assumes 1, 3
                    if dungeon[i][j] == c.FLOOR:
                        if itr == 0:
                            print("___", end='')
                        elif itr == 2:
                            print("---", end='')
                    else:
                        print("|=|", end='')
            print()
    print("=" * (len(dungeon)* 3))

def populate_square_dungeon(dungeon):
    x = random.randint(0, len(dungeon) - c.ROOM_DIMENSION_MIN)
    y = random.randint(0, len(dungeon) - c.ROOM_DIMENSION_MIN)
    length = c.ROOM_DIMENSION_MIN
    for counter in range(c.ROOM_COUNT_DEFAULT):
        for i in range(y, y + length):
            for j in range(x, x + length):
                dungeon[i][j] = c.FLOOR
        prev_x = x
        prev_y = y
        x = random.randint(0, len(dungeon) - c.ROOM_DIMENSION_MIN)
        y = random.randint(0, len(dungeon) - c.ROOM_DIMENSION_MIN)
        for i in range(min(x, prev_x), max(x, prev_x)):
            dungeon[y][i] = c.FLOOR
        for i in range(min(y, prev_y), max(y, prev_y)):
            dungeon[i][x] = c.FLOOR
    return dungeon




def dimension_string(dimension):
    return str(dimension) + 'x' + str(dimension)

def start_dungeon_master():
    print('Booting up the DM')
    while True:
        print('Provide a square dimension for a dungeon to generate: ', end='')
        # TODO Include room dimension, room count parms
        dimension = int(input())
#         TODO add input validaiton
        print('Building you a ' + dimension_string(dimension) + ' dungeon...')
        d = build_dungeon(dimension)
        print_dungeon_tiles(d)
        load_to_xls(d)
        print('Dungeon Successfully Generated')
    print('Shutting down the DM')
#     TODO add config_cache


def build_dungeon(dimension):
    d = create_square_dungeon(dimension)
    populate_square_dungeon(d)
    return d

start_dungeon_master()