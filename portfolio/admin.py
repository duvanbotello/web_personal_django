from django.contrib import admin
from .models import Project

#lo creamos para mostrar los campos especiales
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


# Register your models here.
admin.site.register(Project, ProjectAdmin)