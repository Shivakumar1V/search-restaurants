# Generated by Django 4.2.2 on 2023-06-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_restaurant_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
