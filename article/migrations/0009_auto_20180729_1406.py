# Generated by Django 2.0.7 on 2018-07-29 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180729_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
    ]
