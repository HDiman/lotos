from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('edit', views.edit, name="edit"),
    path('change', views.change, name="change"),
    path('list', views.list, name="list"),
]
