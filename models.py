from django.db import models


class LandingPageEntry(models.Model):
    name = models.CharField(max_length= 75)
    email = models.EmailField()
    
    
    def __str__(self) :
        return f"{self.email}"