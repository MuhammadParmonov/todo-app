# Generated by Django 4.2.6 on 2023-10-29 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-datetime']},
        ),
    ]
