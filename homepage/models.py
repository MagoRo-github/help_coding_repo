from django.db import models

class Homepage (models.Model):
    LINGUAGGIO = 'LN'
    UTILITA = 'UT'

    TIPI = [
        (LINGUAGGIO, 'linguaggio'),
        (UTILITA, 'utilità'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPI, blank=True)
    code = models.CharField(unique=True,max_length=20)
    slug = models.SlugField(max_length=50)
    code_guide = models.CharField(blank=True, max_length=50)
    code_img = models.ImageField(upload_to='static/img/code_img', blank=True, height_field=None, width_field=None, max_length=None)
    code_description = models.TextField(blank=True)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name_plural = "Homes"