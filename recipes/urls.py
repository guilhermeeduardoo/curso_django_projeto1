from django.urls import path
from . import views 
# O ponto indica a pasta recipes.vE a linha inteira esta importando o modulo todo, não  só um arquivo do modulo views

# O <parametro> é o parâmetro a ser seguido pela UR, determinada pela view 


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),    
]

