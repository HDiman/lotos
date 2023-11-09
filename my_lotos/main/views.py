from django.shortcuts import render

# Create your views here.


def index(request):

    data = {
        'item5_0': 'Калининград',

    }

    return render(request, 'main/index.html', context=data)
