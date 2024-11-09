from django.contrib import admin

from app20241105.models import Books, Author, AuthorInfo, Publish

# Register your models here.

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(AuthorInfo)
