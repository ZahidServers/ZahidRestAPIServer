# Generated by Django 3.2.8 on 2022-07-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=255)),
                ('img', models.TextField(default='', max_length=255)),
                ('summary', models.TextField(default='', max_length=255)),
            ],
        ),
    ]
