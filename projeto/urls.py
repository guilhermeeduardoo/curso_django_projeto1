from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static  

# Essa linha de código concatena o urlpatterns com o MEDIA_URL, pra carregar as imagens adicionadas no banco de dados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), 
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Essa linha faz o mesmo com arquivos estaticos, mas, já funcionam sem ela 
