# Generated by Django 3.1.1 on 2020-10-06 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_produtor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ator_nome', models.CharField(max_length=200)),
                ('ator_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AtorSerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_personagem', models.CharField(max_length=200)),
                ('ator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.ator')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.serie')),
            ],
        ),
    ]
