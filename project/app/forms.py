from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label='Search')

class BookForm(forms.ModelForm):
     publish_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
        'placeholder': 'Select a date'
    }))
     price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter price'
    }))
     class Meta:
        model = Book
        fields = ['title','author','publish_date','page','price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author'}),
            'page': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of pages'}),
        }