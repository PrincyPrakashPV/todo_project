from django.urls import path
from . import views

urlpatterns = [

    path('',views.Task_view,name='task_view'),
    path('delete/<int:task_id>',views.delete,name='delete'),
    path('update/<int:task_id>',views.update,name='update')
]