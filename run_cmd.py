import argparse
import config as c
import load_map
import dungeons
# For running the program as a command-line argument

# Check run command for args
argparser = argparse.ArgumentParser(description='Testing argparse')
argparser.add_argument('-c', '--client', nargs="?", type=bool, help='If you would like step by step instructions', default=True)
argparser.add_argument('-d', '--dimension', nargs="?", type=int, help='Enter a square dimension for your dungeon', default=20)
argparser.add_argument('-r', '--room', nargs="?", help='Enter dungeon code for the type of room you would like built', default=c.DUNGEON)
args = vars(argparser.parse_args())

# Prompt for arguments if not already provided by user on execution
dim = 0
room = ''
if args['client']:
    dim = int(input('Enter room dimensions (dimXdim format):\n'))
    c.print_room_codes()
    room = input('Enter a valid code from above:\n')
else:
    dim = args['dimension']
    room = args['room']

# Build the appropriate dungeon, and load to file
d = dungeons.dungeon_builds[room](dim)
load_map.load_dungeon_to_file(d)

