# Generated by Django 3.1.7 on 2021-04-25 09:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=400)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='news_item_images/')),
            ],
        ),
    ]
