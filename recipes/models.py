from django.db import models
from django.contrib.auth.models import User 


# O models, transforma classes em tabelas SQL

# CharField é o mesmo de varchar no SQL

# O BooleanField é usado para campos de escolha, ou é True ou é False, no caso "default" conseidera como padrão que ele não começa como html

# O DateField é um campo de data, em que o auto_now_add faz com o sistema pegue a data de adicionamento e não altera depois

# O auto_now atualiza a data toda vez que uma atualização do sistema

# O def __str__(self):  return self.name serve para modificar o nome de category obejct para o nome colocado em admin

# O on_delete=models.SET_NULL é usado para indicar que quando a receita for excluida o category ficarà nulo e o null=True indica que o campo pode ficar nulo

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(max_length=200)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False) 
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
         Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title