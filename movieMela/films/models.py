from django.db import models

class Films(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    genre = models.CharField(max_length=50)
    directors = models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    release_date = models.DateField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name   

 
