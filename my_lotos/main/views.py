from django.shortcuts import render, redirect
from . data_base import data


# Create your views here.


# Блок по автоматизации процесса
def auto_btn(request):
    return redirect('home')



def index(request):
    return render(request, 'main/index.html', context=data)
