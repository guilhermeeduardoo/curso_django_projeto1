from django.contrib import admin
from .models import Category

# Faz uma classe, para registrar o modelo Category e coloca essa linha admin.site.register(Category, CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin) 

