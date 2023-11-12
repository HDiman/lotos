from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('rlc_1', views.rlc_1, name="rlc_1")
]
