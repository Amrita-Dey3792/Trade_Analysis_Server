# Generated by Django 5.1.6 on 2025-03-07 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trade', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TradeData',
            new_name='Stock',
        ),
    ]
