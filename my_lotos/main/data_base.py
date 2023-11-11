import copy



item = {1: ['Здоровье', 'item1_1', 'item1_2', 'item1_3', 'item1_4', 'item1_5', 'item1_6', 'item1_7', 'item1_8',],
        2: ['Достависта', 'item2_1', 'item2_2', 'item2_3', 'item2_4', 'item2_5', 'item2_6', 'item2_7', 'item2_8',],
        3: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', 'item3_7', 'item3_8',],
        4: ['Питание', 'item4_1', 'item4_2', 'item4_3', 'item4_4', 'item4_5', 'item4_6', 'item4_7', 'item4_8',],
        5: ['Москва', 'Профи', 'Сарафан', 'Кодинг', 'Обучение', 'Планирование', 'Питание', 'Здоровье', 'Достависта',],
        6: ['Сарафан', 'item6_1', 'item6_2', 'item6_3', 'item6_4', 'item6_5', 'item6_6', 'item6_7', 'item6_8',],
        7: ['Планирование', 'item7_1', 'item7_2', 'item7_3', 'item7_4', 'item7_5', 'item7_6', 'item7_7', 'item7_8',],
        8: ['Обучение', 'item8_1', 'item8_2', 'item8_3', 'item8_4', 'item8_5', 'item8_6', 'item8_7', 'item8_8',],
        9: ['Кодинг', 'item9_1', 'item9_2', 'item9_3', 'item9_4', 'item9_5', 'item9_6', 'item9_7', 'item9_8',],
        }

# Пересчитать счет блоков по аналогии с центром
# item_copy = copy.deepcopy(item)
# for i in item:
#     for j in range(9):
#         item_copy[i][j] = 'text'
#
# item_copy[5] = item[3]
# item_copy[3][0] = item_copy[5][1]
# item_copy[6][0] = item_copy[5][2]
# item_copy[9][0] = item_copy[5][3]
# item_copy[8][0] = item_copy[5][4]
# item_copy[7][0] = item_copy[5][5]
# item_copy[4][0] = item_copy[5][6]
# item_copy[1][0] = item_copy[5][7]
# item_copy[2][0] = item_copy[5][8]
#
# item = copy.deepcopy(item_copy)


data = {
    'item1_0': item[1][0],
    'item1_1': item[1][1],
    'item1_2': item[1][2],
    'item1_3': item[1][3],
    'item1_4': item[1][4],
    'item1_5': item[1][5],
    'item1_6': item[1][6],
    'item1_7': item[1][7],
    'item1_8': item[1][8],

    'item2_0': item[2][0],
    'item2_1': item[2][1],
    'item2_2': item[2][2],
    'item2_3': item[2][3],
    'item2_4': item[2][4],
    'item2_5': item[2][5],
    'item2_6': item[2][6],
    'item2_7': item[2][7],
    'item2_8': item[2][8],

    'item3_0': item[3][0],
    'item3_1': item[3][1],
    'item3_2': item[3][2],
    'item3_3': item[3][3],
    'item3_4': item[3][4],
    'item3_5': item[3][5],
    'item3_6': item[3][6],
    'item3_7': item[3][7],
    'item3_8': item[3][8],

    'item4_0': item[4][0],
    'item4_1': item[4][1],
    'item4_2': item[4][2],
    'item4_3': item[4][3],
    'item4_4': item[4][4],
    'item4_5': item[4][5],
    'item4_6': item[4][6],
    'item4_7': item[4][7],
    'item4_8': item[4][8],

    'item5_0': item[5][0],
    'item5_1': item[5][1],
    'item5_2': item[5][2],
    'item5_3': item[5][3],
    'item5_4': item[5][4],
    'item5_5': item[5][5],
    'item5_6': item[5][6],
    'item5_7': item[5][7],
    'item5_8': item[5][8],

    'item6_0': item[6][0],
    'item6_1': item[6][1],
    'item6_2': item[6][2],
    'item6_3': item[6][3],
    'item6_4': item[6][4],
    'item6_5': item[6][5],
    'item6_6': item[6][6],
    'item6_7': item[6][7],
    'item6_8': item[6][8],

    'item7_0': item[7][0],
    'item7_1': item[7][1],
    'item7_2': item[7][2],
    'item7_3': item[7][3],
    'item7_4': item[7][4],
    'item7_5': item[7][5],
    'item7_6': item[7][6],
    'item7_7': item[7][7],
    'item7_8': item[7][8],

    'item8_0': item[8][0],
    'item8_1': item[8][1],
    'item8_2': item[8][2],
    'item8_3': item[8][3],
    'item8_4': item[8][4],
    'item8_5': item[8][5],
    'item8_6': item[8][6],
    'item8_7': item[8][7],
    'item8_8': item[8][8],

    'item9_0': item[9][0],
    'item9_1': item[9][1],
    'item9_2': item[9][2],
    'item9_3': item[9][3],
    'item9_4': item[9][4],
    'item9_5': item[9][5],
    'item9_6': item[9][6],
    'item9_7': item[9][7],
    'item9_8': item[9][8],
}


