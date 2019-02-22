# Generated by Django 2.0.13 on 2019-02-22 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('intro', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(upload_to='', verbose_name='Blogs Image')),
                ('status', models.CharField(choices=[('1', 'Publish'), ('0', 'Unpublished')], max_length=1)),
                ('types', models.CharField(choices=[('1', 'News'), ('0', 'Events')], max_length=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
