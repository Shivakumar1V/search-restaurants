# Generated by Django 4.2.2 on 2023-06-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_restaurant_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
