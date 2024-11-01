import datetime
import os



if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day1030.settings')
    import django
    django.setup()
    from app241031 import models

    book_list = []
    for i in range(20):
        obj = models.Books(
            book_name='葵花宝典第%s套'%i,
            book_price=20+i,
            release_date=datetime.datetime.now(),
            release_address='成华大道%s号'%i
        )
        book_list.append(obj)
    models.Books.objects.bulk_create(book_list)
