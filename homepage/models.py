from django.db import models

class Homepage (models.Model):

    code = models.CharField(max_length=50)
    code_guide = models.CharField(blank=True, max_length=50)
    code_img = models.ImageField(upload_to='static/img/code_img', blank=True, height_field=None, width_field=None, max_length=None)
    code_description = models.TextField(blank=True)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name_plural = "Homes"