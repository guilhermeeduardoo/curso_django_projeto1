from django.db import models

# O models, transforma classes em tabelas SQL

# CharField é o mesmo de varchar no SQL

# O BooleanField é usado para campos de escolha, ou é True ou é False, no caso "default" conseidera como padrão que ele não começa como html

# O DateField é um campo de data, em que o auto_now_add faz com o sistema pegue a data de adicionamento e não altera depois

# O auto_now atualiza a data toda vez que uma atualização do sistema

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_publishied = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
