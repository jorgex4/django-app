# Generated by Django 5.0.2 on 2024-04-27 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='clienteproducto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='clienteproducto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='monto',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 47, 55, 275403)),
        ),
    ]
