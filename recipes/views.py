from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Render faz a função de dar um request e fazer o HttpResponse, colocando o nome do arquivo html a ser renderizado em templates
# recipes = Recipe.objects.all(), é usado para pegar todas as receitas criadas no models, que nem no python shell
# filter(is_published=True), faz com que só apareça as receitas que estejam com o is_published marcado
# O f, é o f string, que passa o argumento como string e o recipes.first().category.name, pega o primeiro nome a ser chamado quando clicado na categoria
# O - Category |, é só pra complemantar o nome da página, junta uma variavel com uma string
# Esse código, if not recipes: raise Http404('Not found :('), foi feito para retornar um 404 e a mensagem "Not found", quando não achar um id de categoria


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipes/pages/home.html',context={
        'recipes': recipes, 
})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not found :(') 

    return render(request,'recipes/pages/category.html',context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category |' 
})

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',context={
        'recipe': make_recipe(),
        'is_detail_page': True, 
})



