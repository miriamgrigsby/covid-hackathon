# Generated by Django 3.2.4 on 2021-06-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tok_name', models.CharField(max_length=50)),
                ('tok_symbol', models.CharField(max_length=50)),
                ('init_supply', models.IntegerField(default='0')),
                ('tok_addr', models.CharField(max_length=50)),
                ('dev_addr', models.CharField(max_length=50)),
                ('dep_time', models.DateTimeField(default='2021-06-19 14:26:03+00')),
            ],
        ),
    ]
