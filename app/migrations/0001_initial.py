# Generated by Django 4.1.7 on 2023-03-29 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='REQUEST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CITY', models.CharField(max_length=40)),
                ('DATE', models.DateTimeField(verbose_name='Date it was requested')),
            ],
        ),
    ]
