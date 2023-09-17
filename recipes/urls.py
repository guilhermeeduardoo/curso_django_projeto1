from django.urls import path
from . import views 
# Oponto indica a pasta recipes.E a linha inteira esta importando o modulo todo, não  só um arquivo do modulo viwes

# O <parametro> é o parâmetro a ser seguido pela UR, determinada pela view 


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),    
]

