# Generated by Django 4.1.7 on 2023-02-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('rollno', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pass1', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]