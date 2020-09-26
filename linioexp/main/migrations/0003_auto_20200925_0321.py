# Generated by Django 3.1.1 on 2020-09-25 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reputacion', models.FloatField(default=0)),
                ('coberturaEntrega', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('documentoIdentidad', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidoPaterno', models.CharField(max_length=20)),
                ('apellidoMaterno', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=1)),
                ('fechaNacimiento', models.DateField()),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=30)),
                ('fechaEntrega', models.DateField()),
                ('direccionEntrega', models.CharField(max_length=50)),
                ('tarifa', models.FloatField(max_length=7)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cliente')),
                ('repartidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.colaborador')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.producto')),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.usuario'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.usuario'),
        ),
    ]