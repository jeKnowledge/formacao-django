from django.urls import path
from .views import list_books, create_book, update_book, delete_book

urlpatterns = [
    path('list/', list_books, name='list_books'),
    path('create/', create_book, name='create_book'),
    path('update/<int:pk>/', update_book, name='update_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book')
]