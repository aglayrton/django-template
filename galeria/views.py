from django.shortcuts import render, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from galeria.models import Galeria

# Create your views here.

dados = {
    1: {'nome':"Galaxia1", "legenda": "nasa"},
    2: {'nome':"Galaxia2", "legenda": "estado"}
}

def index(request):
    #return HttpResponse('<h1>EEEP SITUAÇÃO</h1>')
    #galeria = Galeria.objects.all() traz todos
    #  -fotografia_data o menos inverte a ordem. tambem pode colocar mais filtro .filter(publicada = True).filter(campo = valor)
    galeria = Galeria.objects.order_by("fotografia_data").filter(publicada = True)
    return render(request, 'index.html', {'cards': galeria})

def imagem(request, galeria_id):
    galeria = get_object_or_404(Galeria, pk = galeria_id)
    return render(request, 'imagem.html', {'galeria':galeria})

def buscar(request):
    galeria = Galeria.objects.order_by("fotografia_data").filter(publicada = True)
    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            galeria = galeria.filter(nome__icontains = nome_busca)
    return render(request, "buscar.html", {'cards': galeria})