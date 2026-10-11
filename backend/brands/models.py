# Brand model is now in vehicles app - this file kept for migration compatibility
from django.db import models
import uuid


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name