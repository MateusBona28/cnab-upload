# Generated by Django 4.1.3 on 2022-11-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=26)),
                ('data', models.CharField(max_length=26)),
                ('valor', models.CharField(max_length=26)),
                ('CPF', models.CharField(max_length=11)),
                ('cartao', models.CharField(max_length=26)),
                ('hora', models.CharField(max_length=9)),
                ('dono', models.CharField(max_length=30)),
                ('nome_loja', models.CharField(max_length=26)),
            ],
        ),
    ]
