from django.shortcuts import render
from . data_base import DataSet


# Create your views here.


def index(request):

    data = {
        'item1_0': 'Здоровье',
        'item1_1': 'item1_1',
        'item1_2': 'item1_2',
        'item1_3': 'item1_3',
        'item1_4': 'item1_4',
        'item1_5': 'item1_5',
        'item1_6': 'item1_6',
        'item1_7': 'item1_7',
        'item1_8': 'item1_8',

        'item2_0': 'Достависта',
        'item2_1': 'item2_1',
        'item2_2': 'item2_2',
        'item2_3': 'item2_3',
        'item2_4': 'item2_4',
        'item2_5': 'item2_5',
        'item2_6': 'item2_6',
        'item2_7': 'item2_7',
        'item2_8': 'item2_8',

        'item3_0': 'Профи',
        'item3_1': 'item3_1',
        'item3_2': 'item3_2',
        'item3_3': 'item3_3',
        'item3_4': 'item3_4',
        'item3_5': 'item3_5',
        'item3_6': 'item3_6',
        'item3_7': 'item3_7',
        'item3_8': 'item3_8',

        'item4_0': 'Питание',
        'item4_1': 'item4_1',
        'item4_2': 'item4_2',
        'item4_3': 'item4_3',
        'item4_4': 'item4_4',
        'item4_5': 'item4_5',
        'item4_6': 'item4_6',
        'item4_7': 'item4_7',
        'item4_8': 'item4_8',

        'item5_0': 'Москва',
        'item5_1': 'Профи',
        'item5_2': 'Сарафан',
        'item5_3': 'Кодинг',
        'item5_4': 'Обучение',
        'item5_5': 'Планирование',
        'item5_6': 'Питание',
        'item5_7': 'Здоровье',
        'item5_8': 'Достависта',

        'item6_0': 'Сарафан',
        'item6_1': 'item6_1',
        'item6_2': 'item6_2',
        'item6_3': 'item6_3',
        'item6_4': 'item6_4',
        'item6_5': 'item6_5',
        'item6_6': 'item6_6',
        'item6_7': 'item6_7',
        'item6_8': 'item6_8',

        'item7_0': 'Планирование',
        'item7_1': 'item7_1',
        'item7_2': 'item7_2',
        'item7_3': 'item7_3',
        'item7_4': 'item7_4',
        'item7_5': 'item7_5',
        'item7_6': 'item7_6',
        'item7_7': 'item7_7',
        'item7_8': 'item7_8',

        'item8_0': 'Обучение',
        'item8_1': 'item8_1',
        'item8_2': 'item8_2',
        'item8_3': 'item8_3',
        'item8_4': 'item8_4',
        'item8_5': 'item8_5',
        'item8_6': 'item8_6',
        'item8_7': 'item8_7',
        'item8_8': 'item8_8',

        'item9_0': 'Кодинг',
        'item9_1': 'item9_1',
        'item9_2': 'item9_2',
        'item9_3': 'item9_3',
        'item9_4': 'item9_4',
        'item9_5': 'item9_5',
        'item9_6': 'item9_6',
        'item9_7': 'item9_7',
        'item9_8': 'item9_8',
    }

    return render(request, 'main/index.html', context=data)
