from django.http import HttpResponse
from django.shortcuts import render
# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates 


def home(request):
    return render(request,'recipes/home.html',context={
        'name': 'Guilherme Brito', 
    })

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return render(request,'recipes/contato.html')

