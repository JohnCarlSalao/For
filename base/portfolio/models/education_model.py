from django.db import models

class Education(models.Model):
    school = models.CharField (max_length = 255)
    degree = models.CharField (max_length = 255)
    years = models.CharField (max_length= 255)
    descriptions = models.TextField()
    ordinal = models.IntegerField ()

