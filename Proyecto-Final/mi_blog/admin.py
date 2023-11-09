from django.contrib import admin

from .models import Persona, Familiares, Amigos, Viajes

admin.site.register(Persona)
admin.site.register(Familiares)
admin.site.register(Amigos)
admin.site.register(Viajes)


# Register your models here.
