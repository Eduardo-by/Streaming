# Generated by Django 4.0.3 on 2022-05-16 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0008_filme_filme_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]