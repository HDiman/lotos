from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('edit', views.edit, name="edit"),
    path('edit_2', views.edit_2, name="edit_2"),
    path('list', views.list, name="list"),
]
