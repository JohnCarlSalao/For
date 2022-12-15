from django.db import models

class Portfolio(models.Model):
    title = models.CharField (max_length= 255)
    description = models.TextField()
    image = models.ImageField(upload_to= 'uploads/')
    url = models.URLField ()
    ordinal = models.IntegerField ()