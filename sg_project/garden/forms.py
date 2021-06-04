from django import forms

from .models import Field, Topic


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'description', 'review_frequency']



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']