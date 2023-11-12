import copy


item_0 = {0: ['Москва', 'Профи', 'Сарафан', 'Кодинг', 'Обучение', 'Планирование', 'Питание', 'Здоровье', 'Достависта',],
         1: ['Профи', 'Поиск заказов', 'Переписка', 'Продажа', 'Ремонт', 'Инструмент', 'Запчасти', 'item1_7', 'item1_8',],
         2: ['Сарафан', 'item2_1', 'item2_2', 'item2_3', 'item2_4', 'item2_5', 'item2_6', 'item2_7', 'item2_8',],
         3: ['Кодинг', 'item3_1', 'item3_2', 'item3_3', 'item3_4', 'item3_5', 'item3_6', 'item3_7', 'item3_8',],
         4: ['Обучение', 'item4_1', 'item4_2', 'item4_3', 'item4_4', 'item4_5', 'item4_6', 'item4_7', 'item4_8',],
         5: ['Планирование', 'item5_1', 'item5_2', 'item5_3', 'item5_4', 'item5_5', 'item5_6', 'item5_7', 'item5_8',],
         6: ['Питание', 'item6_1', 'item6_2', 'item6_3', 'item6_4', 'item6_5', 'item6_6', 'item6_7', 'item6_8',],
         7: ['Здоровье', 'item7_1', 'item7_2', 'item7_3', 'item7_4', 'item7_5', 'item7_6', 'item7_7', 'item7_8',],
         8: ['Достависта', 'item8_1', 'item8_2', 'item8_3', 'item8_4', 'item8_5', 'item8_6', 'item8_7', 'item8_8',],
        }



# Переход листка в центр

def replace(item, n):
    item_copy = copy.deepcopy(item)
    for i in item_copy:
        for j in range(9):
            item_copy[i][j] = ''

    item_copy[0] = item[n]
    item_copy[1][0] = item_copy[0][1]
    item_copy[2][0] = item_copy[0][2]
    item_copy[3][0] = item_copy[0][3]
    item_copy[4][0] = item_copy[0][4]
    item_copy[5][0] = item_copy[0][5]
    item_copy[6][0] = item_copy[0][6]
    item_copy[7][0] = item_copy[0][7]
    item_copy[8][0] = item_copy[0][8]

    item = copy.deepcopy(item_copy)
    return item


for i in range(4):
    num = int(input('Выберите блок: '))
    item = replace(item_0, num)
    for j in item:
        print(item[j])



