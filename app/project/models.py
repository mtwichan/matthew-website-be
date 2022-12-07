from django.db import models
from martor.models import MartorField

STATUS = ((0, "DRAFT"), (1, "PUBLISH"))

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    preview_img = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    content = MartorField()
    description = models.TextField(default="project preview...")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("project_detail", kwargs={"slug": str(self.slug)})