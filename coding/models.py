from django.db import models

from homepage.models import Homepage

class Coding(models.Model):
    linguaggio = models.ForeignKey(Homepage,to_field='code' ,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, blank=True)

    argomento = models.CharField(max_length=50, default='')

    snippet = models.TextField(default='')

    def __str__(self):
        return f'{self.argomento} ({self.linguaggio})'
    