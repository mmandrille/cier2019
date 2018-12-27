# Generated by Django 2.1.3 on 2018-12-27 05:06

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo')),
                ('portada', models.FileField(default='/archivos/defaults/noimage.gif', upload_to='eventos/portadas/')),
                ('descripcion', tinymce.models.HTMLField()),
                ('fecha_inicio', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha del Evento')),
                ('fecha_fin', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de fin del Evento')),
                ('importante', models.BooleanField(default=False)),
            ],
        ),
    ]
