# Generated by Django 5.1.7 on 2025-04-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('características', models.TextField()),
                ('tecnologias', models.TextField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='proyectos/')),
                ('enlace', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
