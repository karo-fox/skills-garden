from django import forms

from .models import TextSource, URLSource


class TextSourceForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = TextSource
        fields = ['name', 'content']



class URLSourceForm(forms.ModelForm):
    content = forms.URLField(label="Source link")

    class Meta:
        model = URLSource
        fields = ['name', 'content']