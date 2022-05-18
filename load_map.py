import config as c
import xlsxwriter
import random as r
import json

# Pass in file types you wish to load
def load_dungeon_to_file(dungeon, file_options):
    if all(x in c.LOAD_ALL_FILES for x in c.LOAD_JSON):
        load_to_json(dungeon)
    if all(x in c.LOAD_ALL_FILES for x in c.LOAD_XLSX):
        load_to_xls(dungeon)

def load_to_json(dungeon):
    relative_path = c.DUNGEON_JSON_ROOT + str(r.randint(1, 1000)) + c.DUNGEON_FILE_JSON
    data = dict()
    data['dungeon'] = dungeon
    json_data = json.dumps(data)
    try:
        f = open(relative_path, 'w')
        f.write(json_data)
    except {FileExistsError, FileNotFoundError} as e:
        print(e)
    print('Loaded dungeon to ' + relative_path)

def load_to_xls(dungeon):
    relative_path = c.DUNGEON_XLSX_ROOT + str(r.randint(1, 1000)) + c.DUNGEON_FILE_XLSX
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