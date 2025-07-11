# Generated by Django 5.0.2 on 2025-05-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0009_alter_eventos_cupo_maximo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='cupo_maximo',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='descripcion',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
