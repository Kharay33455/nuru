# Generated by Django 5.1.1 on 2024-09-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_mosque_latitude_alter_mosque_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosque',
            name='zoom',
            field=models.FloatField(default=10.0),
        ),
    ]
