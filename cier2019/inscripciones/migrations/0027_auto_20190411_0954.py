# Generated by Django 2.1.3 on 2019-04-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0026_auto_20190406_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscriptos',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='direccion_laboral',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='email_laboral',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='lugar_trabajo',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='ocupacion',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='profesion',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='telefono_laboral',
        ),
        migrations.RemoveField(
            model_name='inscriptos',
            name='web',
        ),
    ]