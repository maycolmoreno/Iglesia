# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-15 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id_detallefactura', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_uni', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cant_adultos', models.IntegerField()),
                ('cant_ninos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id_detallereserva', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=30)),
                ('precio_uni', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cant_adultos', models.IntegerField()),
                ('cant_ninos', models.IntegerField()),
                ('id_tipohabitacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('id_reserva', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('numero_factura', models.CharField(max_length=15)),
                ('estado_factura', models.BooleanField()),
                ('dias', models.IntegerField()),
                ('id_persona', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id_galeria', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='galeria')),
                ('nombre_imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('numero_habitacion', models.IntegerField()),
                ('piso_habitacion', models.IntegerField()),
                ('estado_habitacion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('barrio', models.CharField(max_length=15)),
                ('e_civil', models.CharField(max_length=2000, verbose_name='Estado Civil')),
                ('f_nac', models.DateField()),
                ('estado', models.BooleanField()),
                ('genero', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateField(auto_now_add=True)),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('dias', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('abono', models.BooleanField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id_tipohabitacion', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='tiposHab')),
                ('nombre_tipo', models.CharField(max_length=100)),
                ('precio_tipo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('nro_personas', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Tipo Habitaciones',
            },
        ),
        migrations.AddField(
            model_name='habitacion',
            name='tipohabitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.TipoHabitacion'),
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Reserva'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Habitacion'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Servicio'),
        ),
    ]
