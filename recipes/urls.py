from django.urls import path
from . import views 
# O ponto indica a pasta recipes.vE a linha inteira esta importando o modulo todo, não  só um arquivo do modulo views

# O <parametro> é o parâmetro a ser seguido pela UR, determinada pela view 

# O name="", é usado para dar nomes unicos as URLS


app_name = 'recipes' # app_name:name, é a variavel com o nome da url

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),    
]

