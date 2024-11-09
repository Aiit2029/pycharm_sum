from django.http import HttpResponse
from django.shortcuts import render

from app20241105 import models


# Create your views here.


def query(request):

    # models.Author.objects.create(
    #     auth_name = '',
    #     auth_age = '',
    #     author_info=''
    #
    # )
    # book_lst = models.Books.objects.filter(publish__pub_name='这也算是出版社').values_list('book_name','book_price')
    # for i in book_lst:
    #     print(i)
    # book_lst = models.Publish.objects.filter(pub_name='这也算是出版社').values_list('books__book_name','books__book_price')
    # for i in book_lst:
    #     print(i)
    # dep_name = models.emp.objects.values(dep__id).values_list('name').annotate(c = Count(emp__id))

    return HttpResponse('ok')