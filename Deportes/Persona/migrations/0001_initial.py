# Generated by Django 5.0.6 on 2024-07-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('genero', models.CharField(max_length=100)),
                ('disiplina', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Juez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('genero', models.CharField(max_length=100)),
                ('disiplina', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
