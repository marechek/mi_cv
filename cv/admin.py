from django.contrib import admin

from .models import (
    Profile,
    Experiencia,
    Logro,
    Educacion,
    Habilidad,
    Idioma
)


class LogroInline(admin.TabularInline):
    model = Logro
    extra = 1


class ExperienciaAdmin(admin.ModelAdmin):
    inlines = [LogroInline]


admin.site.register(Profile)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(Educacion)
admin.site.register(Habilidad)
admin.site.register(Idioma)
