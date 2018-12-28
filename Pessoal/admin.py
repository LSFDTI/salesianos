from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Dados_base, Documento 

admin.site.register(Documento)
admin.site.register(Dados_base)