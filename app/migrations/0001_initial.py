# Generated by Django 5.0.4 on 2024-04-13 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_details', models.TextField(max_length=100)),
                ('task_type', models.CharField(choices=[('panding', 'panding'), ('done', 'done')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Mobile', models.IntegerField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.task')),
            ],
        ),
    ]