from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# isso só existe pq quero que no Admin apareça o campo filmes_vistos, mas ele estava funcionando normalmente.
campos = list(UserAdmin.fieldsets)
campos.append(("Históricos", {'fields': ('filmes_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
