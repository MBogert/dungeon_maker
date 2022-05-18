import config as c
import xlsxwriter
from os.path import exists
import json
import random as r

# Pass in file types you wish to load
# .json or .xlsx
def load_dungeon_to_file(dungeon, name, file_options=['json', 'xlsx']):
    if 'json' in file_options:
        load_to_json(dungeon, name)
    if 'xlsx' in file_options:
        load_to_xls(dungeon, name)

def load_to_json(dungeon, name):
    relative_path = 'dungeons/json/' + name + '_dungeon.json'
    # Quietly handle duplicate filenames
    if exists(relative_path):
        relative_path = 'dungeons/json/' + name + str(r.randint(0, 1000)) + '_dungeon.json'
    data = dict()
    data['dungeon'] = dungeon
    json_data = json.dumps(data)
    try:
        f = open(relative_path, 'w')
        f.write(json_data)
    except {FileExistsError, FileNotFoundError} as e:
        print(e)
    print('Loaded dungeon to ' + relative_path)

def load_to_xls(dungeon, name):
    relative_path = 'dungeons/xlsx/' + name + '_dungeon.xlsx'
    # Quietly handle duplicate filenames
    if exists(relative_path):
        relative_path = 'dungeons/xlsx/' + name + str(r.randint(0, 1000)) + '_dungeon.xlsx'
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
