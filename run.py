import dungeons
import config as c
import os
import random as r
import load_map

def run():
    while True:
        if input('Would you like to create a dungeon? (y/n)\n') == 'n':
            break
        num_rooms = int(input('How many rooms would you like to make? (generating more than one room will build a campaign)\n'))
        if num_rooms == 1:
            # Retrieve values for a single room
            dim = int(input('How large is your dungeon (dimXdim format):\n'))
            c.print_room_codes()
            room = input('What type of dungeon would you like built:\n')
            name = input('What is your dungeon called:\n')
            d = dungeons.dungeon_builds[room](dim)
            load_map.load_dungeon_to_file(d, name)
        else:
            # Build a dungeon campaign
            rooms = []
            # Collect information for each room
            for i in range(0, num_rooms):
                print('Now building room ' + str(i + 1))
                dim = int(input('How large is your dungeon (dimXdim format):\n'))
                c.print_room_codes()
                room = input('What type of dungeon would you like built:\n')
                name = input('What is your dungeon called:\n')
                d = dungeons.dungeon_builds[room](dim)
                rooms.append((name, d))
            # Create the directory to store room-files
            name = input('What will the name of your campaign be?\n')
            relative_path = ('campaigns/' + name + '/') if os.path.exists('campaigns/' + name + '/') is not True else ('campaigns/' + name + '_' + str(r.randint(0, 1000)) + '/')
            os.makedirs(relative_path)
            # Build each room's files
            for room in rooms:
                load_map.load_dungeon_to_campaign(room[1], room[0], relative_path)
            print('Campaign can be found at ' + relative_path)
    print('Goodbye')
run()
