import config as c
import random



def create_square_dungeon(dimension):
    return [[c.WALL] * dimension] * dimension

def print_dungeon(dungeon):
    print("= " * len(dungeon))
    for row in dungeon:
        print(*row, sep=" ")
    print("= " * len(dungeon))

def populate_square_dungeon(dungeon):
    x = random.randint(0, len(dungeon) - 5)
    y = random.randint(0, len(dungeon) - 5)
    length = c.ROOM_DIMENSION_MIN
    for counter in range(c.ROOM_COUNT_DEFAULT):
        for i in range(y, y + length):
            for j in range(x, x + length):
                dungeon[i][j] = c.FLOOR
        x = random.randint(0, len(dungeon) - 5)
        y = random.randint(0, len(dungeon) - 5)
    return dungeon

def run():
    d = create_square_dungeon(c.DIMENSION_DEFAULT)
    populate_square_dungeon(d)
    print_dungeon(d)

run()