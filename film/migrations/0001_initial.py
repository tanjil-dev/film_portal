# Generated by Django 3.2.4 on 2024-07-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('movie_link', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'films',
            },
        ),
    ]
