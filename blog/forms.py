import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Category


class BlogForm(forms.Form):
    title = forms.CharField(label="Название", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"class": "form-control",
                                                                          "rows": 7
                                                                          }))
    category = forms.ModelChoiceField(label="Категория", empty_label="Выберите категорию",
                                      queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))
    photo = forms.ImageField(label="Фото", widget=forms.FileInput(attrs={"class": "form-control"}))
    is_published = forms.BooleanField(label="Опубликовать запись?", initial=True)

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
