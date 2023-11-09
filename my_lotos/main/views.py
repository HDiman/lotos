from django.shortcuts import render

# Create your views here.


def index(request):

    data = {
        'item5_0': 'Москва',
        'item5_1': 'Профи',
        'item5_2': 'Сарафан',
        'item5_3': 'Кодинг',
        'item5_4': 'Обучение',
        'item5_5': 'Планирование',
        'item5_6': 'Питание',
        'item5_7': 'Здоровье',
        'item5_8': 'Достависта',

        'item3_0': 'Профи',
        'item3_1': 'item3_1',
        'item3_2': 'item3_2',
        'item3_3': 'item3_3',
        'item3_4': 'item3_4',
        'item3_5': 'item3_5',
        'item3_6': 'item3_6',
        'item3_7': 'item3_7',
        'item3_8': 'item3_8',

    }

    return render(request, 'main/index.html', context=data)
