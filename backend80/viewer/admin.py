from django.contrib import admin
from viewer.models import Genre, Movie, ShortUrls
from viewer.views import hello

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(ShortUrls)


