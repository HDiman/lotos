from django.shortcuts import render, redirect
from . data_base import data


def rlc_1(request):
    return redirect('home')


def index(request):
    return render(request, 'main/index.html', context=data)
