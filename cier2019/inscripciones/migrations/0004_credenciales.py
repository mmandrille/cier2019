# Generated by Django 2.1.3 on 2018-12-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0003_auto_20181227_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credenciales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL_BACKEND', models.CharField(max_length=100, verbose_name='EMAIL_BACKEND')),
                ('EMAIL_HOST', models.CharField(max_length=100, verbose_name='EMAIL_HOST')),
                ('EMAIL_PORT', models.IntegerField(default=587)),
                ('EMAIL_USE_TLS', models.BooleanField(default=True)),
                ('EMAIL_HOST_USER', models.CharField(max_length=100, verbose_name='EMAIL_HOST_USER')),
                ('DEFAULT_FROM_EMAIL', models.CharField(max_length=100, verbose_name='DEFAULT_FROM_EMAIL')),
                ('SERVER_EMAIL', models.CharField(max_length=100, verbose_name='SERVER_EMAIL')),
                ('EMAIL_HOST_PASSWORD', models.CharField(max_length=100, verbose_name='EMAIL_HOST_PASSWORD')),
            ],
        ),
    ]