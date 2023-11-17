from django.shortcuts import render, redirect
from .models import Grid


# список данных в grid
def list(request):
    grid = Grid.objects.all()
    data = {"grid": grid}
    return render(request, 'main/list.html', context=data)


# изменение данных в бд
def edit(request, id):
    grid = Grid.objects.get(id=id)
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
    else:
        data = {
            'grid_0': Grid.objects.all()[0],
            'grid_1': Grid.objects.all()[1],
            'grid_2': Grid.objects.all()[2],
            'grid_3': Grid.objects.all()[3],
            'grid_4': Grid.objects.all()[4],
            'grid_5': Grid.objects.all()[5],
            'grid_6': Grid.objects.all()[6],
            'grid_7': Grid.objects.all()[7],
            'grid_8': Grid.objects.all()[8],
            }
        return render(request, 'main/edit.html', context=data)


def index(request):
    data = {
        'grid_0': Grid.objects.all()[0],
        'grid_1': Grid.objects.all()[1],
        'grid_2': Grid.objects.all()[2],
        'grid_3': Grid.objects.all()[3],
        'grid_4': Grid.objects.all()[4],
        'grid_5': Grid.objects.all()[5],
        'grid_6': Grid.objects.all()[6],
        'grid_7': Grid.objects.all()[7],
        'grid_8': Grid.objects.all()[8],
        }

    return render(request, 'main/index.html', context=data)
