from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import  RichTextField 

# Create your models here.

# MODELO CATEGORIA


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    active = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name

# MODELO ETIQUETAS


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    active = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiqueta"
        ordering = ["name"]

    def __str__(self):
        return self.name


# MODELO AUTHOR - USUARIO REFISTRADO EN LA APLICACION -> llamamos la tabla usuarios


# MODELO DE LOS POST
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    excerpt = models.TextField(verbose_name="Bajada")
    # content = models.TextField(verbose_name="Contenido")
    content =  RichTextField(verbose_name="Contenido")
    image = models.ImageField(
        upload_to="Post", null=True, blank=True, verbose_name="Imagen")
    published = models.BooleanField(default=False, verbose_name="Publicado")

    # Campos con relaciones
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='get_post', verbose_name="Categoria")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='get_post', verbose_name="Autor")
    tags = models.ManyToManyField(Tag, verbose_name="Etiquetas")

    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.title

####
#   OTRAS TABLAS
#####


class About(models.Model):
    descriptions = models.CharField(
        max_length=350, null=True, verbose_name="Descripción")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Acerca de"
        verbose_name_plural = "Acerca de Nosotros"
        ordering = ["-created"]

    def __str__(self):
        return self.descriptions


class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name="key link")
    name = models.CharField(max_length=120, verbose_name="Red social")
    url = models.CharField(max_length=350, null=True,
                        blank=True, verbose_name="Enlace")
    icon = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name="Icon")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["name"]

    def __str__(self):
        return self.name
