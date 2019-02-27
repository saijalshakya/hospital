# Generated by Django 2.0.13 on 2019-02-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_booking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.CharField(default='0', max_length=10000),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.CharField(choices=[('1', 'Paid'), ('0', 'Unpaid')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='source',
            field=models.CharField(choices=[('1', 'Cash'), ('2', 'Credit Card'), ('3', 'Master Card')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(default='0', max_length=1000),
        ),
    ]