from django.contrib import admin
from .models import Usuario,Sigue,Categoria,Pertenece


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Sigue)
admin.site.register(Categoria)
admin.site.register(Pertenece)