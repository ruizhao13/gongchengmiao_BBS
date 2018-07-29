# Generated by Django 2.0.7 on 2018-07-28 05:35

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('is_school_info', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('ueditor_body', DjangoUeditor.models.UEditorField(null=True, verbose_name='内容')),
                ('isElite', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, default='django-db-models-fields-charfield', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PostRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.IntegerField(default=0)),
                ('post_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost')),
            ],
        ),
    ]
