from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField(default=None)
    review_frequency = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('garden:field-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'models.Field({self.name}, {self.description}, {self.date_added}, {self.last_reviewed}, {self.review_frequency})'
    
    def admin_topic_filter_link(self):
        return mark_safe(f'<a href="/admin/garden/topic/?field__id__exact={self.id}">topics</a>')


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField(default=None)

    def get_absolute_url(self):
        return reverse('garden:topic-detail', kwargs={'field_pk': self.field.id, 'pk': self.id})

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'models.Topic({self.name}, {self.description}, {self.field}, {self.date_added}, {self.last_reviewed})'

    def admin_field_link(self):
        return mark_safe(f'<a href="/admin/garden/field/{self.field.id}/change/">{self.field.name}</a>')