from django.shortcuts import render, redirect
# from .data_base import data
from .models import Grid




def rlc_1(request):
    return redirect('home')


def index(request):
    main_item = Grid.objects.all()

    data = {
        'item0_0': main_item[0],

    }

    return render(request, 'main/index.html', context=data)
