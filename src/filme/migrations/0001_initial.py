# Generated by Django 4.0.3 on 2022-05-07 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
                ('views_count', models.IntegerField(default=0)),
                ('imagem', models.ImageField(upload_to='filmes')),
                ('ano_de_producao', models.DateField()),
                ('status', models.CharField(choices=[('RA', 'Recem Adicionado'), ('MA', 'Mais Assistidos'), ('TR', 'Top Rated')], max_length=2)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filme.categoria')),
                ('lingua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filme.lingua')),
            ],
        ),
    ]
