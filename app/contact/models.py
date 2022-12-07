from django.db import models
from martor.models import MartorField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        subject = f"{self.affiliation} - {self.name} - {self.email}"
        content = self.message
        return f"{subject} \n {content}"