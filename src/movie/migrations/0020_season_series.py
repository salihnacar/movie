# Generated by Django 4.1.2 on 2022-10-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_series_seasons'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='series',
            field=models.ManyToManyField(related_name='Series', to='movie.series'),
        ),
    ]
