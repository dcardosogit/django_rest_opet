from django.contrib import admin
from .models import Serie,Episodio,Review,Produtor,Ator,AtorSerie
# Register your models here.

admin.site.register(Serie)
admin.site.register(Episodio)
admin.site.register(Review)
admin.site.register(Produtor)
admin.site.register(Ator)
admin.site.register(AtorSerie)