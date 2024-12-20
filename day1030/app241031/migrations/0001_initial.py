# Generated by Django 5.1.2 on 2024-11-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=32)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('release_date', models.DateField()),
                ('release_address', models.CharField(max_length=32)),
            ],
        ),
    ]
