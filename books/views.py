from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Books, Category

# Create your views here.
def home(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/home.html', context)

def detail_book(request, id):
    book = get_object_or_404(Books, id=id)

    context = {
        'book': book,
    }

    return render(request, 'books/detail.html', context)    