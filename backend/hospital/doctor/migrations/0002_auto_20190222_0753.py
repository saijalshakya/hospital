# Generated by Django 2.0.13 on 2019-02-22 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('1', 'Publish'), ('0', 'Unpublished')], max_length=1, null=True)),
                ('soft', models.BooleanField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='type',
            field=models.ManyToManyField(to='doctor.Type'),
        ),
    ]