# Generated by Django 3.2.9 on 2021-11-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_calificacion', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('id_producto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_comentario', models.IntegerField()),
                ('date_comment', models.DateTimeField(verbose_name='Fecha de creacion')),
                ('rate_comment', models.IntegerField()),
                ('comment', models.CharField(default='', max_length=70)),
                ('user', models.CharField(max_length=70)),
                ('email_user', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pregunta', models.IntegerField()),
                ('date_pregunta', models.DateTimeField(verbose_name='Fecha de creacion')),
                ('pregunta', models.CharField(default='', max_length=70)),
                ('user', models.CharField(max_length=70)),
                ('email_user', models.CharField(max_length=70)),
            ],
        ),
    ]
