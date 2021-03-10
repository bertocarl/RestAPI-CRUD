from django.contrib import admin
from .models import Movie


class ProjectAdmin(admin.ModelAdmin):
    


# Register your models here.
    admin.site.register(Movie)