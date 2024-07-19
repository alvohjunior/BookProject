from django import forms

from books.models import AnimeBooks


class AnimeBooksForm(forms.ModelForm):
    class Meta:
        model = AnimeBooks
        fields = '__all__'


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = AnimeBooks

    fields = '__all__'


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = AnimeBooks
        fields = '__all__'
