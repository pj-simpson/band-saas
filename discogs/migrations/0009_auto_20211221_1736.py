# Generated by Django 3.1.7 on 2021-12-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discogs', '0008_auto_20211220_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='table_header_color',
            field=models.CharField(default='#FFFFFF', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discogs.format'),
        ),
    ]
