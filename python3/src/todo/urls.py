from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('regist', views.regist, name='regist'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
]