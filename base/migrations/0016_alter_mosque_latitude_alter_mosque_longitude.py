# Generated by Django 5.1.1 on 2024-09-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_mosque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosque',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
