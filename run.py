import dungeons
import config as c
import os
import random as r
import load_map
import dungeon_cli

def run():
    while True:
        if input('Would you like to create a dungeon? (y/n)\n') == 'n':
            break
        num_rooms = int(input('How many rooms would you like to make? (generating more than one room will build a campaign)\n'))
        if num_rooms == 1:
            dungeon_cli.build_single_dungeon()
        else:
            dungeon_cli.build_campaign(num_rooms)
    print('Goodbye')
run()
