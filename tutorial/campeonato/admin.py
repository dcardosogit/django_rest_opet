from django.contrib import admin
from .models import Time, Jogador, Jogo, Campeonato
# Register your models here.

admin.site.register(Time)
admin.site.register(Jogador)
admin.site.register(Jogo)
admin.site.register(Campeonato)