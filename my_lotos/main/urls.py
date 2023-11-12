from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('rlc_0', views.rlc_0, name="rlc_0"),
    path('rlc_1', views.rlc_1, name="rlc_1")
]
