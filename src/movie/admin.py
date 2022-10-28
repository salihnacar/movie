from django.contrib import admin
from .models import MovieType, Movie, Subtitle, Actor, Series, Season, Epsoide

# Register your models here.
admin.site.register(MovieType)
admin.site.register(Movie)
admin.site.register(Subtitle)
admin.site.register(Actor)
admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Epsoide)