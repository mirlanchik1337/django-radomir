from django.urls import path
from . import views


urlpatterns = [
    path('books_list/', views.books_list_view, name='books_list'),


]