from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app241031 import models


# Create your views here.
def main(request):
    all_obj = models.Books.objects.all()

    return render(request, 'books.html', {'all_obj': all_obj})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    else:
        print(request.POST)
        title = request.POST.get('book_title')
        price = request.POST.get('book_price')
        pub_date = request.POST.get('book_date')
        publish = request.POST.get('book_publish')

        models.Books.objects.create(
            book_name=title,
            book_price=price,
            release_date=pub_date,
            release_address=publish,
        )
        return redirect(reverse('main'))


def delete_book(request, book_id):
    models.Books.objects.filter(id=book_id).delete()
    return redirect(reverse('main'))


def edit_book(request, book_id):
    if request.method == "GET":
        obj = models.Books.objects.get(id=book_id)
        return render(request, 'edit_book.html', {'obj': obj})
    else:
        title = request.POST.get('book_title')
        price = request.POST.get('book_price')
        pub_date = request.POST.get('book_date')
        publish = request.POST.get('book_publish')
        models.Books.objects.filter(id=book_id).update(
            book_name=title,
            book_price=price,
            release_date=pub_date,
            release_address=publish,
        )
        return redirect(reverse('main'))
