import config as c
import xlsxwriter
import random as r


def load_to_xls(dungeon):
    relative_path = c.DUNGEON_DIRECTORY + str(r.randint(1, 1000)) + c.DUNGEON_FILE_DEFAULT
    workbook = xlsxwriter.Workbook(relative_path)
    worksheet = workbook.add_worksheet()
    cell_format_floor = workbook.add_format()
    cell_format_floor.set_bg_color('white')
    # cell_format_floor.set_font_color('white')
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
