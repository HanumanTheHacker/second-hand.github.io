# Generated by Django 4.1.7 on 2023-03-03 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='designation',
            new_name='details',
        ),
    ]