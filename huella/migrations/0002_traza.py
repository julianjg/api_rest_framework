# Generated by Django 3.0.7 on 2020-07-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huella', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_id', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
