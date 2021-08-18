
from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    tags=models.TextField()
    img=models.FileField(upload_to="pic/%y/")
    def __str__(self):
        return self.title
    class Meta  :
        ordering=('-id',)    

    def get_absolute_url(self):
        return reverse('details',args=[self.id,self.slug])    