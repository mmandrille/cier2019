# Generated by Django 2.1.3 on 2019-04-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0028_inscriptos_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptos',
            name='activo',
            field=models.BooleanField(default=False, verbose_name='Mail Validado'),
        ),
    ]