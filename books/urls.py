from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('mark-as-read/<int:id>/', views.mark_as_read, name='mark_as_read'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    #path('toggle-read/<int:id>/', views.toggle_read_status, name='toggle_read_status'),
]
