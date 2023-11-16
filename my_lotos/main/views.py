from django.shortcuts import render, redirect
# from .data_base import data
from .models import Grid



# изменение данных
def change(request):
    grid = Grid.objects.get(id=3)
    if request.method == 'POST':
        grid.item_0 = request.POST.get('item_0')
        grid.item_1 = request.POST.get('item_1')
        grid.item_2 = request.POST.get('item_2')
        grid.item_3 = request.POST.get('item_3')
        grid.item_4 = request.POST.get('item_4')
        grid.item_5 = request.POST.get('item_5')
        grid.item_6 = request.POST.get('item_6')
        grid.item_7 = request.POST.get('item_7')
        grid.item_8 = request.POST.get('item_8')
        grid.save()
    return redirect('home')


# изменение данных в grid_2
def list(request):
    grid = Grid.objects.all()
    data = {"grid": grid}
    return render(request, 'main/list.html', context=data)


# изменение данных в бд
def edit(request):
    grid_0 = Grid.objects.all()[0]
    grid_1 = Grid.objects.all()[1]
    grid_2 = Grid.objects.all()[2]
    grid_3 = Grid.objects.all()[3]
    grid_4 = Grid.objects.all()[4]
    grid_5 = Grid.objects.all()[5]
    grid_6 = Grid.objects.all()[6]
    grid_7 = Grid.objects.all()[7]
    grid_8 = Grid.objects.all()[8]

    data = {
        'item0_0': grid_0.item_0,
        'item0_1': grid_0.item_1,
        'item0_2': grid_0.item_2,
        'item0_3': grid_0.item_3,
        'item0_4': grid_0.item_4,
        'item0_5': grid_0.item_5,
        'item0_6': grid_0.item_6,
        'item0_7': grid_0.item_7,
        'item0_8': grid_0.item_8,

        'item1_0': grid_1.item_0,
        'item1_1': grid_1.item_1,
        'item1_2': grid_1.item_2,
        'item1_3': grid_1.item_3,
        'item1_4': grid_1.item_4,
        'item1_5': grid_1.item_5,
        'item1_6': grid_1.item_6,
        'item1_7': grid_1.item_7,
        'item1_8': grid_1.item_8,

        'item2_0': grid_2.item_0,
        'item2_1': grid_2.item_1,
        'item2_2': grid_2.item_2,
        'item2_3': grid_2.item_3,
        'item2_4': grid_2.item_4,
        'item2_5': grid_2.item_5,
        'item2_6': grid_2.item_6,
        'item2_7': grid_2.item_7,
        'item2_8': grid_2.item_8,

        'item3_0': grid_3.item_0,
        'item3_1': grid_3.item_1,
        'item3_2': grid_3.item_2,
        'item3_3': grid_3.item_3,
        'item3_4': grid_3.item_4,
        'item3_5': grid_3.item_5,
        'item3_6': grid_3.item_6,
        'item3_7': grid_3.item_7,
        'item3_8': grid_3.item_8,

        'item4_0': grid_4.item_0,
        'item4_1': grid_4.item_1,
        'item4_2': grid_4.item_2,
        'item4_3': grid_4.item_3,
        'item4_4': grid_4.item_4,
        'item4_5': grid_4.item_5,
        'item4_6': grid_4.item_6,
        'item4_7': grid_4.item_7,
        'item4_8': grid_4.item_8,

        'item5_0': grid_5.item_0,
        'item5_1': grid_5.item_1,
        'item5_2': grid_5.item_2,
        'item5_3': grid_5.item_3,
        'item5_4': grid_5.item_4,
        'item5_5': grid_5.item_5,
        'item5_6': grid_5.item_6,
        'item5_7': grid_5.item_7,
        'item5_8': grid_5.item_8,

        'item6_0': grid_6.item_0,
        'item6_1': grid_6.item_1,
        'item6_2': grid_6.item_2,
        'item6_3': grid_6.item_3,
        'item6_4': grid_6.item_4,
        'item6_5': grid_6.item_5,
        'item6_6': grid_6.item_6,
        'item6_7': grid_6.item_7,
        'item6_8': grid_6.item_8,

        'item7_0': grid_7.item_0,
        'item7_1': grid_7.item_1,
        'item7_2': grid_7.item_2,
        'item7_3': grid_7.item_3,
        'item7_4': grid_7.item_4,
        'item7_5': grid_7.item_5,
        'item7_6': grid_7.item_6,
        'item7_7': grid_7.item_7,
        'item7_8': grid_7.item_8,

        'item8_0': grid_8.item_0,
        'item8_1': grid_8.item_1,
        'item8_2': grid_8.item_2,
        'item8_3': grid_8.item_3,
        'item8_4': grid_8.item_4,
        'item8_5': grid_8.item_5,
        'item8_6': grid_8.item_6,
        'item8_7': grid_8.item_7,
        'item8_8': grid_8.item_8,
    }
    # if id == 3:
    return render(request, 'main/edit.html', context=data)
    # else:
    #     return redirect('home')


def index(request):
    grid_0 = Grid.objects.all()[0]
    grid_1 = Grid.objects.all()[1]
    grid_2 = Grid.objects.all()[2]
    grid_3 = Grid.objects.all()[3]
    grid_4 = Grid.objects.all()[4]
    grid_5 = Grid.objects.all()[5]
    grid_6 = Grid.objects.all()[6]
    grid_7 = Grid.objects.all()[7]
    grid_8 = Grid.objects.all()[8]

    data = {
        'item0_0': grid_0.item_0,
        'item0_1': grid_0.item_1,
        'item0_2': grid_0.item_2,
        'item0_3': grid_0.item_3,
        'item0_4': grid_0.item_4,
        'item0_5': grid_0.item_5,
        'item0_6': grid_0.item_6,
        'item0_7': grid_0.item_7,
        'item0_8': grid_0.item_8,

        'item1_0': grid_1.item_0,
        'item1_1': grid_1.item_1,
        'item1_2': grid_1.item_2,
        'item1_3': grid_1.item_3,
        'item1_4': grid_1.item_4,
        'item1_5': grid_1.item_5,
        'item1_6': grid_1.item_6,
        'item1_7': grid_1.item_7,
        'item1_8': grid_1.item_8,

        'item2_0': grid_2.item_0,
        'item2_1': grid_2.item_1,
        'item2_2': grid_2.item_2,
        'item2_3': grid_2.item_3,
        'item2_4': grid_2.item_4,
        'item2_5': grid_2.item_5,
        'item2_6': grid_2.item_6,
        'item2_7': grid_2.item_7,
        'item2_8': grid_2.item_8,

        'item3_0': grid_3.item_0,
        'item3_1': grid_3.item_1,
        'item3_2': grid_3.item_2,
        'item3_3': grid_3.item_3,
        'item3_4': grid_3.item_4,
        'item3_5': grid_3.item_5,
        'item3_6': grid_3.item_6,
        'item3_7': grid_3.item_7,
        'item3_8': grid_3.item_8,

        'item4_0': grid_4.item_0,
        'item4_1': grid_4.item_1,
        'item4_2': grid_4.item_2,
        'item4_3': grid_4.item_3,
        'item4_4': grid_4.item_4,
        'item4_5': grid_4.item_5,
        'item4_6': grid_4.item_6,
        'item4_7': grid_4.item_7,
        'item4_8': grid_4.item_8,

        'item5_0': grid_5.item_0,
        'item5_1': grid_5.item_1,
        'item5_2': grid_5.item_2,
        'item5_3': grid_5.item_3,
        'item5_4': grid_5.item_4,
        'item5_5': grid_5.item_5,
        'item5_6': grid_5.item_6,
        'item5_7': grid_5.item_7,
        'item5_8': grid_5.item_8,

        'item6_0': grid_6.item_0,
        'item6_1': grid_6.item_1,
        'item6_2': grid_6.item_2,
        'item6_3': grid_6.item_3,
        'item6_4': grid_6.item_4,
        'item6_5': grid_6.item_5,
        'item6_6': grid_6.item_6,
        'item6_7': grid_6.item_7,
        'item6_8': grid_6.item_8,

        'item7_0': grid_7.item_0,
        'item7_1': grid_7.item_1,
        'item7_2': grid_7.item_2,
        'item7_3': grid_7.item_3,
        'item7_4': grid_7.item_4,
        'item7_5': grid_7.item_5,
        'item7_6': grid_7.item_6,
        'item7_7': grid_7.item_7,
        'item7_8': grid_7.item_8,

        'item8_0': grid_8.item_0,
        'item8_1': grid_8.item_1,
        'item8_2': grid_8.item_2,
        'item8_3': grid_8.item_3,
        'item8_4': grid_8.item_4,
        'item8_5': grid_8.item_5,
        'item8_6': grid_8.item_6,
        'item8_7': grid_8.item_7,
        'item8_8': grid_8.item_8,
    }

    return render(request, 'main/index.html', context=data)
