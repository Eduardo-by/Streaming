# Generated by Django 4.0.3 on 2022-05-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0004_alter_filme_categoria_alter_filme_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ação', 'Ação'), ('romance', 'Romance'), ('ficção', 'Ficção'), ('terror', 'Terror'), ('aventura', 'Aventura'), ('suspense', 'Suspense'), ('anime', 'Anime')], max_length=9),
        ),
        migrations.AlterField(
            model_name='filme',
            name='lingua',
            field=models.CharField(choices=[('BR', 'Brasil'), ('EUA', 'Estados Unidos'), ('EU', 'Europa'), ('JP', 'Japão')], max_length=3),
        ),
        migrations.DeleteModel(
            name='Lingua',
        ),
    ]
