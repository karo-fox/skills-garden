from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # user = models.ForeignKey(User)
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField()
    review_frequency = models.DurationField()

    def __str__(self):
        return f'Field: {self.name} - {self.review_frequency} - {self.last_reviewed}'
    
    def __repr__(self):
        return f'models.Field({self.name}, {self.description}, {self.date_added}, {self.last_reviewed}, {self.review_frequency})'


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField()

    def __str__(self):
        return f'Topic: {self.name} - {self.field.name} - {self.last_reviewed}'
    
    def __repr__(self):
        return f'models.Topic({self.name}, {self.description}, {self.field}, {self.date_added}, {self.last_reviewed})'