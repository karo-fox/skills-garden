from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500)
    by_system = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'