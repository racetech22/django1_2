from django.shortcuts import render
from django.shortcuts import get_object_or_404



from  .models import Produto

# Create your views here.

def index(request):
    produtos =  Produto.objects.all()
    context = {
        'curso' : 'Programação Web com Django Framework',
        'pedra' : 'pedra',
        'produtos' : produtos
    }
    return render(request, 'index.html' , context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = get_object_or_404(Produto, pk=pk)

    context = {
        'produto':prod
    }
    return render(request, 'produto.html', context)

