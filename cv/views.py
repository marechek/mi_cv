from django.shortcuts import render

from .models import (
    Profile,
    Experiencia,
    Educacion,
    Habilidad,
    Idioma
)


def index(request):

    profile = Profile.objects.first()

    experiencias = Experiencia.objects.all()

    educaciones = Educacion.objects.all()

    habilidades = Habilidad.objects.all()

    idiomas = Idioma.objects.all()

    context = {
        "profile": profile,
        "experiencias": experiencias,
        "educaciones": educaciones,
        "habilidades": habilidades,
        "idiomas": idiomas
    }

    return render(request, "cv/index.html", context)
