# Generated by Django 4.1.7 on 2024-11-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_apellidos_usuario_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
    ]
