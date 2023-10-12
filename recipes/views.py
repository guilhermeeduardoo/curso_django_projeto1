from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates
# recipes = Recipe.objects.all(), é usado para pegar todas as receitas criadas no models, que nem no python shell


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes, 
})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes, 
})

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',context={
        'recipe': make_recipe(),
        'is_detail_page': True, 
})



