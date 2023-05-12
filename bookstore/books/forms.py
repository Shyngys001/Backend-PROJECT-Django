from django.forms import ModelForm, TextInput, Textarea
from books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'image_url', 'follow_author', 'book_available', 'genre']

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        return book
