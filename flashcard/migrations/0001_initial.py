# Generated by Django 3.1.6 on 2021-02-12 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_one', models.TextField()),
                ('side_two', models.TextField()),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='set.set')),
            ],
        ),
    ]
