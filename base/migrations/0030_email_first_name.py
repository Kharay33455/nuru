# Generated by Django 5.1.1 on 2024-10-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_mailerror'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='first_name',
            field=models.CharField(default='Guest', max_length=50),
        ),
    ]