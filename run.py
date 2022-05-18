import dungeons
import config as c
import load_map

def run():
    while True:
        if input('Would you like to create a dungeon? (y/n)\n') == 'n':
            break
        dim = int(input('How large is your dungeon (dimXdim format):\n'))
        c.print_room_codes()
        room = input('What type of dungeon would you like built:\n')
        name = input('What is your dungeon called:\n')
        d = dungeons.dungeon_builds[room](dim)
        load_map.load_dungeon_to_file(d, name)
        print('Goodbye')
run()
