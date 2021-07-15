from django.db import models

from garden.models import Field

class Revision(models.Model):
    date = models.DateField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def is_active(self):
        return self.field.last_reviewed <= self.date