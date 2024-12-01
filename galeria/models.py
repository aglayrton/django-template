from datetime import datetime
from django.db import models

# Create your models here.
class Galeria(models.Model):
    
    OPCOES = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    
    nome = models.CharField(max_length=30, blank = False)
    legenda = models.CharField(max_length=100, blank = False)
    descricao = models.TextField()
    foto = models.CharField(max_length=30, blank = False)
    categoria = models.CharField(max_length=100, choices = OPCOES, default='')
    publicada = models.BooleanField(default=False)
    fotografia_data = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self) -> str:
        return f"Galeria com nome:{self.nome}"