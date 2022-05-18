import argparse
import config as c
import load_map
import dungeons

# Check run command for args
argparser = argparse.ArgumentParser(description='Testing argparse')
argparser.add_argument('-c', '--client', nargs="?", type=bool, help='If you would like step by step instructions', default=False)
argparser.add_argument('-d', '--dimension', nargs="?", type=int, help='Enter a square dimension for your dungeon', default=20)
argparser.add_argument('-r', '--room', nargs="?", help='Enter dungeon code for the type of room you would like built', default=c.DUNGEON)
args = vars(argparser.parse_args())

# Prompt for arguments if not already provided by user on execution
if args['client'] or (args['dimension'] == None or args['room']):
    print('client path')
else:
    dim = args['dimension']
    room = args['room']
    d = dungeons.dungeon_builds[room](dim)
    load_map.load_dungeon_to_file(d)