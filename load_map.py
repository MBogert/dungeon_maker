import config as c
import xlsxwriter
from os.path import exists
import json
import random as r

def load_dungeon_to_file(dungeon, name='generic_filename'):
    load_to_json(dungeon, name, 'dungeons/json/')
    load_to_xls(dungeon, name, 'dungeons/xlsx/')

def load_dungeon_to_campaign(dungeon, dungeon_name, relative_path_base):
    load_to_json(dungeon, dungeon_name, relative_path_base)
    load_to_xls(dungeon, dungeon_name, relative_path_base)

def load_to_json(dungeon, name, relative_path_base):
    relative_path = (relative_path_base + name + '.json') if exists(relative_path_base + name + '.json') is not True else (relative_path_base + name + '_' + str(r.randint(0, 1000)) + '.json')
    data = dict()
    data['dungeon'] = dungeon
    json_data = json.dumps(data)
    try:
        f = open(relative_path, 'w')
        f.write(json_data)
    except {FileExistsError, FileNotFoundError} as e:
        print(e)
    print('Loaded dungeon to ' + relative_path)

def load_to_xls(dungeon, name, relative_path_base):
    relative_path = (relative_path_base + name + '.xlsx') if exists(relative_path_base + name + '.xlsx') is not True else (relative_path_base + name + '_' + str(r.randint(0, 1000)) + '.xlsx')
    workbook = xlsxwriter.Workbook(relative_path)
    worksheet = workbook.add_worksheet()
    cell_format_floor = workbook.add_format()
    cell_format_floor.set_bg_color('white')
    cell_format_wall = workbook.add_format()
    cell_format_wall.set_bg_color('black')
    for i in range(len(dungeon)):
        for j in range(len(dungeon)):
            if dungeon[i][j] == c.FLOOR:
                worksheet.write(i, j, dungeon[i][j], cell_format_floor)
            elif dungeon[i][j] == c.WALL:
                worksheet.write(i, j, dungeon[i][j], cell_format_wall)
            else:
                print('Invalid Code Detected')
    workbook.close()
    print('Loaded dungeon to ' + relative_path)
