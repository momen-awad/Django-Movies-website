# Generated by Django 3.2.9 on 2021-11-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(null=True, to='movie.Cast'),
        ),
    ]
