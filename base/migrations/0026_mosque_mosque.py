# Generated by Django 5.1.1 on 2024-10-02 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_remove_mosque_latitude_remove_mosque_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosque',
            name='mosque',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.address'),
            preserve_default=False,
        ),
    ]
