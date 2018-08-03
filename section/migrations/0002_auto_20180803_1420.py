# Generated by Django 2.0.6 on 2018-08-03 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionadministrator',
            name='forum_administrator_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sectionadministrator',
            name='forum_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.SectionForum'),
        ),
    ]
