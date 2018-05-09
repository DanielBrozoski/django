from django.contrib import admin
from .models import *

admin.site.register(Evento)
admin.site.register(Atividade)
admin.site.register(PapelNoEvento)
admin.site.register(Pessoa)
admin.site.register(Tag)