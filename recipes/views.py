from django.shortcuts import render
# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates 


def home(request):
    return render(request,'recipes/home.html',context={
        'name': 'Guilherme Brito', 
    })



