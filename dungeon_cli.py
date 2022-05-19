import config as c
import dungeons
import load_map
import os
import random as r

# Command-line approach to building dungeons

def build_single_dungeon():
    d = dungeon_builder_command_line()
    load_map.load_dungeon_to_file(d[0], d[1])

def build_campaign(num_rooms):
    rooms = []
    # Collect information for each room
    for i in range(0, num_rooms):
        print('Now building room ' + str(i + 1))
        d = dungeon_builder_command_line()
        rooms.append((d[1], d[0]))
    # Create the directory to store room-files
    name = input('What will the name of your campaign be?\n')
    relative_path = ('campaigns/' + name + '/') if os.path.exists('campaigns/' + name + '/') is not True else (
                'campaigns/' + name + '_' + str(r.randint(0, 1000)) + '/')
    os.makedirs(relative_path)
    # Build each room's files
    for room in rooms:
        load_map.load_dungeon_to_campaign(room[1], room[0], relative_path)
    print('Campaign can be located at ' + relative_path)

# Prompt user for values to build a single room
def dungeon_builder_command_line():
    dim = int(input('How large is your dungeon (dimXdim format):\n'))
    c.print_room_codes()
    room = input('What type of dungeon would you like built:\n')
    name = input('What is your dungeon called:\n')
    return (dungeons.dungeon_builds[room](dim), name)