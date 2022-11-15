from django.contrib import admin
from django.db import models
from .models import Project

from martor.widgets import AdminMartorWidget
from martor.models import MartorField

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        MartorField: {"widget": AdminMartorWidget},
        models.TextField: {"widget": AdminMartorWidget}
    }

admin.site.register(Project, ProjectAdmin)
