# Generated by Django 2.1.5 on 2019-02-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190216_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('1', 'Publish'), ('0', 'Unpublished')], max_length=1, null=True),
        ),
    ]
