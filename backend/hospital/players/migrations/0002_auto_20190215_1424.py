# Generated by Django 2.1.5 on 2019-02-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='image',
            field=models.FileField(upload_to='', verbose_name='User Image'),
        ),
    ]