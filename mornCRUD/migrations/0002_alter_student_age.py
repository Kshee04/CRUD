# Generated by Django 4.1.7 on 2023-02-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mornCRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
