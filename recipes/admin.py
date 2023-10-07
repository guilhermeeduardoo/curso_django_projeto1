from django.contrib import admin
from .models import Category, Recipe

# Faz uma classe, para registrar o modelo Category e coloca essa linha admin.site.register(Category, CategoryAdmin)

# @admin.register(Recipe) é outra forma de registrar um model no banco de dados, usando o decorate

class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RcipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin) 

