# Generated by Django 2.1.3 on 2019-03-21 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0021_auto_20190321_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='id',
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='progress_url',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inscripciones.Progress_Links'),
        ),
    ]
