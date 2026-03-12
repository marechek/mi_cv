from django.db import models


class Profile(models.Model):

    nombre = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    foto = models.ImageField(upload_to="static/img", blank=True, null=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):

    cargo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)

    fecha_inicio = models.CharField(max_length=50)
    fecha_fin = models.CharField(max_length=50, blank=True)

    descripcion = models.TextField()

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class Logro(models.Model):

    experiencia = models.ForeignKey(
        Experiencia,
        on_delete=models.CASCADE,
        related_name="logros"
    )

    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Logro"
        verbose_name_plural = "Logros"

    def __str__(self):
        return self.descripcion


class Educacion(models.Model):

    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)

    fecha_inicio = models.CharField(max_length=50)
    fecha_fin = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"


class Habilidad(models.Model):

    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nombre


class Idioma(models.Model):

    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField()

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.nombre