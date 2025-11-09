from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skill_rating = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - ({self.skill_rating}/5)"