# Generated by Django 5.1.1 on 2024-10-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_download_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=11)),
                ('bank_name', models.CharField(max_length=50)),
            ],
        ),
    ]
