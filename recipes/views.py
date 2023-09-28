from django.shortcuts import render
# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates
from utils.recipes.factory import make_recipe 


def home(request):
    return render(request,'recipes/pages/home.html',context={
        'recipes': [make_recipe() for _ in range(10)], 
})

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',context={
        'recipe': make_recipe(),
        'is_detail_page': True, 
})



