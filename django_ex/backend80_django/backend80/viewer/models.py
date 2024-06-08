from django.db.models import Model, CharField, DO_NOTHING,\
    DateField, ForeignKey, IntegerField, TextField,\
    DateTimeField

# Create your models here.
class Genre(Model):
    name = CharField(max_length = 128)

class Movie(Model):
    title = CharField(max_length = 128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

class ShortUrls(Model):
    url = CharField(max_length = 4096)
    short_url = CharField(max_length = 8)

