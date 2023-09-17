from django.shortcuts import render
# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates 


def home(request):
    return render(request,'recipes/pages/home.html',context={
        'name': 'Guilherme Brito', 
})

def recipe(request,id):
    return render(request,'recipes/pages/home.html',context={
        'name': 'Guilherme Brito', 
})



