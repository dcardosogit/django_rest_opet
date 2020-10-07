# Generated by Django 3.1.1 on 2020-10-07 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogo_nome', models.CharField(max_length=200)),
                ('jogo_genero', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_nome', models.CharField(max_length=200)),
                ('time_ano_fundacao', models.IntegerField()),
                ('time_sede', models.CharField(max_length=200)),
                ('time_jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonato.jogo')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador_nome', models.CharField(max_length=200)),
                ('jogador_idade', models.IntegerField()),
                ('jogador_abates', models.IntegerField()),
                ('jogador_mortes', models.IntegerField()),
                ('jogador_assistencias', models.IntegerField()),
                ('jogador_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonato.time')),
            ],
        ),
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campeonato_nome', models.CharField(max_length=200)),
                ('campeonato_premiacao', models.FloatField()),
                ('campeonato_inicio', models.DateField()),
                ('campeonato_times', models.ManyToManyField(to='campeonato.Time')),
            ],
        ),
    ]
