from django.urls import path
from market import views

urlpatterns = [
    path('books/', views.view_of_books, name='book-list'),
    path('books/<int:book_id>/', views.view_of_one_book, name='book-detail'),
]
