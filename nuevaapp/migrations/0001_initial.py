# Generated by Django 4.2.5 on 2023-10-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=80)),
                ('actividad', models.CharField(max_length=80)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
