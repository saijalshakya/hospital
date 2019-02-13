# Generated by Django 2.1.5 on 2019-02-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=800)),
                ('image', models.ImageField(blank=True, upload_to='doctor_image')),
                ('age', models.CharField(max_length=200)),
                ('phone1', models.CharField(max_length=800)),
                ('phone2', models.CharField(max_length=800, null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('statement', models.CharField(max_length=5000)),
                ('educationStatement', models.CharField(max_length=5000)),
                ('status', models.BooleanField(default=0)),
                ('soft', models.BooleanField(default=1)),
            ],
        ),
    ]
