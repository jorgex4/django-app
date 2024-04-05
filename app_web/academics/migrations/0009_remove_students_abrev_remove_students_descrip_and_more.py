# Generated by Django 5.0.2 on 2024-04-05 21:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0008_cities_countries_departments_students_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='abrev',
        ),
        migrations.RemoveField(
            model_name='students',
            name='descrip',
        ),
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='id_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academics.user'),
        ),
        migrations.AddField(
            model_name='students',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='id_person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.CharField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='departments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='students',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 5, 16, 52, 53, 247693)),
        ),
    ]
