# Generated by Django 4.2.17 on 2024-12-05 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='original_url',
        ),
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
        migrations.AddField(
            model_name='url',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='url',
            name='expires_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='url',
            name='full_url',
            field=models.URLField(default='hello', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='tiny_url',
            field=models.CharField(default='hello', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
