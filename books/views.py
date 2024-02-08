from django.http import HttpResponse
from django.shortcuts import render
from . import models


def books_list_view(request):
    books = models.Book.objects.all()

    return render(request, 'books_list.html', {'books': books})
