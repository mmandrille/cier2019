# Generated by Django 2.1.3 on 2019-03-21 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0024_auto_20190321_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='progress_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='inscripciones.Progress_Links'),
        ),
    ]