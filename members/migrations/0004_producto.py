# Generated by Django 4.1.7 on 2024-12-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_usuario_apellido_usuario_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precio_Compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_Alquiler', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
