# Generated by Django 4.1.7 on 2024-12-11 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_carrito_carritoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritoitem',
            name='modo',
        ),
    ]
