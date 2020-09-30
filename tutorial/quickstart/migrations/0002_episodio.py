# Generated by Django 3.1.1 on 2020-09-29 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episodio_titulo', models.CharField(max_length=200)),
                ('episodio_avaliacao', models.FloatField()),
                ('episodio_serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.serie')),
            ],
        ),
    ]
