from django.contrib import admin
from galeria.models import Galeria

class ListaGaleria(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10
    
    
    
admin.site.register(Galeria, ListaGaleria)
