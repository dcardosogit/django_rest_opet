from django.db import models

# Create your models here.

'''
Jogo:
- Nome do jogo
- Gênero do Jogo
'''

class Jogo(models.Model):
    jogo_nome = models.CharField(max_length = 200)
    jogo_genero = models.CharField(max_length = 200)

    def __str__(self):
        return self.jogo_nome

'''
Time:
- Nome do time
- Ano de Fundação
- Sede (Cidade)
'''

class Time(models.Model):
    time_nome = models.CharField(max_length = 200)
    time_ano_fundacao = models.IntegerField()
    time_sede = models.CharField(max_length = 200)

    time_jogo = models.ForeignKey(Jogo,on_delete=models.CASCADE)

    def __str__(self):
        return self.time_nome

'''
Jogador:
- Nome do Jogador
- Idade
- Abates
- Mortes
- Assistências
'''

class Jogador(models.Model):
    jogador_nome = models.CharField(max_length = 200)
    jogador_idade = models.IntegerField()
    jogador_abates = models.IntegerField()
    jogador_mortes = models.IntegerField()
    jogador_assistencias = models.IntegerField()

    jogador_time = models.ForeignKey(Time,on_delete=models.CASCADE)

    def __str__(self):
        return self.jogador_nome

'''
Campeonato:
- Nome do campeonato
- Valor total em premiação
- Data de inicio
'''
class Campeonato(models.Model):
    campeonato_nome = models.CharField(max_length = 200)
    campeonato_premiacao = models.FloatField()
    campeonato_inicio = models.DateField()

    campeonato_times = models.ManyToManyField(Time)

    def __str__(self):
        return self.campeonato_nome