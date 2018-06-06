# Generated by Django 2.0.1 on 2018-06-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Huespedes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('appelido_materno', models.CharField(max_length=100)),
                ('appelido_paterno', models.CharField(max_length=100)),
                ('reservaciones_id_huesped', models.ManyToManyField(to='reservaciones.Reservaciones')),
            ],
        ),
    ]