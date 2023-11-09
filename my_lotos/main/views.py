from django.shortcuts import render
from . data_base import data


# Create your views here.


def index(request):
    return render(request, 'main/index.html', context=data)
