from django.shortcuts import render

from app241031 import models


# Create your views here.
def main(request):
    all_obj = models.Books.objects.all()

    return render(request, 'books.html', {'all_obj': all_obj})


def edit_book(request):


    return render(request, 'edit_book.html')


def delete(request):
    pass
