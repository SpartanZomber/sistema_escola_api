# Generated by Django 5.0.2 on 2025-03-17 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0003_alumnos_maestros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnos',
            old_name='clave_alumno',
            new_name='matricula',
        ),
        migrations.RenameField(
            model_name='maestros',
            old_name='clave_maestro',
            new_name='id_trabajador',
        ),
    ]
