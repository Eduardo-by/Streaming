# Generated by Django 4.0.3 on 2022-05-08 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='atores',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FilmeLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD'), ('A', 'ASSISTIR')], max_length=1)),
                ('link', models.URLField()),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filme_assista_link', to='filme.filme')),
            ],
        ),
    ]