# Generated by Django 2.1.5 on 2019-02-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='status',
            field=models.CharField(choices=[('Publish', 'Inside KTM Valley'), ('Unpublish', 'Outside KTM Valley'), ('w', 'Whole Nepal')], max_length=1, null=True),
        ),
    ]
