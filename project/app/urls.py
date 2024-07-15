from django.urls import path
from .views import book_create,book_list,book_update,book_delete,book_search

urlpatterns = [
    path('',book_list,name='book_list'),
    path('create/',book_create,name='book_create'),
    path('update/<int:id>/',book_update,name='book_update'),
    path('delete/<int:id>/',book_delete,name='book_delete'),
    path('search/',book_search,name='book_search')
]