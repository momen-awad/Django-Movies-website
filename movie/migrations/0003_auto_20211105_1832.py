# Generated by Django 3.2.9 on 2021-11-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20211105_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='production_date',
            field=models.DateTimeField(null=True),
        ),
    ]