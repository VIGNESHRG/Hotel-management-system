# Generated by Django 4.0.5 on 2022-10-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_hotels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='img',
        ),
        migrations.AddField(
            model_name='hotels',
            name='field_name',
            field=models.TextField(default=1, verbose_name=40),
            preserve_default=False,
        ),
    ]
