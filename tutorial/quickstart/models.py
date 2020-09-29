from django.db import models

# Create your models here.
class Serie(models.Model):
    serie_titulo = models.CharField(max_length = 200)
    serie_temporadas = models.IntegerField(default=1)
    serie_genero = models.CharField(max_length = 50)

    def __str__(self):
        return self.serie_titulo