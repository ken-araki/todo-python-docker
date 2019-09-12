from django.db import models
from django.forms import ModelForm

class Todo(models.Model):
    todo_id = models.AutoField(
      primary_key=True,
      max_length=10,
    )
    title = models.CharField(
      verbose_name='TODOタイトル',
      max_length=50
    )
    detail = models.CharField(
      verbose_name='TODO詳細',
      max_length=300
    )
    insert_date = models.DateTimeField(
      'date published',
      auto_now_add=True,
    )
    update_date = models.DateTimeField(
      'date published',
      auto_now=True,
    )

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_id', 'title', 'detail', 'insert_date', 'update_date']
        exclude = ['todo_id', 'insert_date', 'update_date']