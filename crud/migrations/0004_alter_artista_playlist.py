# Generated by Django 4.2.1 on 2023-06-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_concierto_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='playlist',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Playlist'),
        ),
    ]