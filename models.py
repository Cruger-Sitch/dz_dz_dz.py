from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    published_date = models.DateTimeField('Date published')

    def __str__(self)-> str:
        return f'{self.title} by {self.content}'

