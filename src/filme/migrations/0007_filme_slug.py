# Generated by Django 4.0.3 on 2022-05-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0006_alter_filme_lingua'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]