# Generated by Django 5.0.2 on 2025-05-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0005_eventos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventos',
            old_name='horario',
            new_name='hora_final',
        ),
        migrations.AddField(
            model_name='eventos',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
