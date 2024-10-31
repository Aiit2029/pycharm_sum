# Generated by Django 5.1.2 on 2024-10-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('current_date', models.DateField()),
            ],
        ),
    ]