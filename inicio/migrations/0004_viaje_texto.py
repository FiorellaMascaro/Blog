# Generated by Django 4.2.5 on 2023-10-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_alter_viaje_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='texto',
            field=models.CharField(default='', max_length=500),
        ),
    ]