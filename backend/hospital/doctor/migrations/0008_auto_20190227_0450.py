# Generated by Django 2.0.13 on 2019-02-27 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20190226_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='Anonymous', max_length=10000),
        ),
    ]
