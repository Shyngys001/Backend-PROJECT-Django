from random import choice
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):

    GENRE_CHOICES = (
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('sci-fi', 'Science Fiction'),
        ('romance', 'Romance'),
        ('none', 'none'),
        # add more genre options as needed
    )

  

    genre = django_filters.ChoiceFilter(label='Genre', choices=GENRE_CHOICES)

    class Meta:
        model = Book
        fields = {
            'genre': ['exact']
        }
