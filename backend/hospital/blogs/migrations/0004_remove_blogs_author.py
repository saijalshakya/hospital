# Generated by Django 2.1.5 on 2019-02-16 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190216_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='author',
        ),
    ]