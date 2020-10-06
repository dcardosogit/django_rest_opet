from django.db import models

# Create your models here.
class Serie(models.Model):
    serie_titulo = models.CharField(max_length = 200)
    serie_temporadas = models.IntegerField(default=1)
    serie_genero = models.CharField(max_length = 50)

    def __str__(self):
        return self.serie_titulo

class Episodio(models.Model):
    episodio_serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    episodio_titulo = models.CharField(max_length = 200)
    episodio_avaliacao = models.FloatField()

    def __str__(self):
        return self.episodio_titulo

class Review(models.Model):
    review_serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    review_titulo = models.CharField(max_length = 200)
    review_texto = models.TextField()
    review_avaliacao = models.FloatField()

    def __str__(self):
        return self.review_titulo

class Produtor(models.Model):
    produtor_nome = models.CharField(max_length = 200)
    produtor_series = models.ManyToManyField(Serie)

    def __str__(self):
        return self.produtor_nome

class Ator(models.Model):
    ator_nome = models.CharField(max_length = 200)
    ator_nascimento = models.DateField()

    def __str__(self):
        return self.ator_nome

class AtorSerie(models.Model):
    ator = models.ForeignKey(Ator,on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    nome_personagem = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome_personagem
