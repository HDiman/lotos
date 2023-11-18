from django.shortcuts import render, redirect
from .models import Grid
from .forms import UserForms


# список данных в grid
def list(request):
    grid = Grid.objects.all()
    data = {"grid": grid}
    return render(request, 'main/list.html', context=data)


# изменение данных в бд + валидация данных
def edit(request, id):
    grid = Grid.objects.get(id=id)
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            grid.item_0 = form.cleaned_data['item_0']
            grid.item_1 = form.cleaned_data['item_1']
            grid.item_2 = form.cleaned_data['item_2']
            grid.item_3 = form.cleaned_data['item_3']
            grid.item_4 = form.cleaned_data['item_4']
            grid.item_5 = form.cleaned_data['item_5']
            grid.item_6 = form.cleaned_data['item_6']
            grid.item_7 = form.cleaned_data['item_7']
            grid.item_8 = form.cleaned_data['item_8']
            grid.save()
        return redirect('home')
    else:
        data = {
            'id': id,
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
