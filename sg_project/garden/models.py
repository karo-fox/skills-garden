from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(User)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    last_reviewed = models.DateField()
    review_frequency = models.DurationField()

    def __str__(self):
        return f'"{self.name}" in field "{self.field}"'