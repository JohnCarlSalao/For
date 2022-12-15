from django.db import models
class Work(models.Model):
    company = models.CharField (max_length=255)
    years = models.CharField (max_length=255)
    description = models.TextField()
    summary = models.TextField()
    ordinal = models.IntegerField()
    
