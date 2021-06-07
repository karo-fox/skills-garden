from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # user = models.ForeignKey(User)
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField(auto_now=True)
    review_frequency = models.IntegerField()

    def get_absolute_url(self):
        return reverse('client:field', kwargs={'pk': self.id})

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
    last_reviewed = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('client:topic', kwargs={'field_pk': self.field.id, 'pk': self.id})

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'models.Topic({self.name}, {self.description}, {self.field}, {self.date_added}, {self.last_reviewed})'

    def admin_field_link(self):
        return mark_safe(f'<a href="/admin/garden/field/{self.field.id}/change/">{self.field.name}</a>')