from django.contrib import admin
from .models import *
# # Register your models here.

# Categorias


class Categoryadmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['name', 'active', 'created']


admin.site.register(Category, Categoryadmin)


# Etiquetas
class Tagadmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['name', 'active', 'created']


admin.site.register(Tag, Tagadmin)


# Post publicaciones
class Postadmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = [
        'title',
        'category',
        'author',
        'created'
    ]
    ordering = ["author", "-created"]
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author', 'category', 'tags')


admin.site.register(Post, Postadmin)


# About
class Aboutadmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['descriptions', 'created']


admin.site.register(About, Aboutadmin)


# Link
class Linkadmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['key', 'name', 'url']


admin.site.register(Link, Linkadmin)
