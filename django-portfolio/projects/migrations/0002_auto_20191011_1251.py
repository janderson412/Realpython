# Generated by Django 2.2.6 on 2019-10-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/projects/img'),
        ),
    ]
