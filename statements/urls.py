from django.urls import path
from . import views

app_name = 'statements'

urlpatterns = [
    path('', views.index, name='index'),
    path('leave/', views.leave, name='leave'),
    path('add_leave/', views.add_leave, name='add_leave'),
    path('delete_leave/<int:leave_id>', views.delete_leave, name='delete_leave'),
    path('teachers/', views.teachers_name, name='teachers_name'),
]