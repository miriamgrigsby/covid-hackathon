# Generated by Django 3.0.4 on 2020-04-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidfitness', '0022_auto_20200329_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedchallenge',
            name='photo',
            field=models.ImageField(blank=True, upload_to='challenge_photos'),
        ),
    ]