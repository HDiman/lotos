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


item_copy = copy.deepcopy(item)
for i in item:
    for j in range(9):
        item_copy[i][j] = 'text'

item_copy[5] = item[3]

item_copy[3][0] = item_copy[5][1]
item_copy[6][0] = item_copy[5][2]
item_copy[9][0] = item_copy[5][3]
item_copy[8][0] = item_copy[5][4]
item_copy[7][0] = item_copy[5][5]
item_copy[4][0] = item_copy[5][6]
item_copy[1][0] = item_copy[5][7]
item_copy[2][0] = item_copy[5][8]



for i in item_copy:
    print(item_copy[i])



