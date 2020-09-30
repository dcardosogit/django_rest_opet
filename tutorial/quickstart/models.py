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