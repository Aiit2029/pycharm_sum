from django.db import models

# Create your models here.


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=32)
    book_price = models.DecimalField(max_digits=8,decimal_places=2)
    release_date = models.DateField()
    release_address = models.CharField(max_length=32)


