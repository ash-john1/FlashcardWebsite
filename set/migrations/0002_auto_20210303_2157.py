# Generated by Django 3.1.6 on 2021-03-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]