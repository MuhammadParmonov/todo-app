# Generated by Django 4.2.6 on 2023-10-29 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.category'),
        ),
    ]
