# Generated by Django 4.1.7 on 2023-03-11 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_category_point_parent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='point',
            new_name='branch',
        ),
    ]
