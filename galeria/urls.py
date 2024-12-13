from django.urls import path # type: ignore
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:galeria_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar")
]