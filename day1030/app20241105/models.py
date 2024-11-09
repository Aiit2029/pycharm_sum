from django.db import models


# Create your models here.



class AuthorInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    auth_birth = models.DateField()
    auth_phonenum = models.BigIntegerField()
    auth_address = models.CharField(max_length=64)

    def __str__(self):

        return f'{self.nid}号作者'

class Author(models.Model):

    nid = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=16)
    auth_age = models.IntegerField()

    author_info = models.OneToOneField(to='AuthorInfo', to_field='nid', on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.auth_name}'



class Publish(models.Model):

    nid = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=16)
    pub_address = models.CharField(max_length=16)
    pub_email = models.EmailField(max_length=254, verbose_name='电子邮箱', null=True, blank=True)

    def __str__(self):

        return self.pub_name

class Books(models.Model):

    nid = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=32)
    book_pub_date = models.DateField()
    book_price = models.DecimalField(max_digits=8,decimal_places=2)

    publish = models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)

    authors = models.ManyToManyField(to=Author)




    def __str__(self):
        return self.book_name