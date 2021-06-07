from django.db import models

from garden.models import Topic



class Source(models.Model):
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)



class TextSource(Source):
    content = models.TextField()



class URLSource(Source):
    content = models.URLField()