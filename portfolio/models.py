from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Experience
class Experience(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['publish']
        indexes = [
            models.Index(fields=['publish'])
        ]
    def __str__(self):
        return f'{self.title}'

# Education
class Education(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['publish']
        indexes = [
            models.Index(fields=['publish'])
        ]

    def __str__(self):
        return f'{self.title}'

# Testimonials
class Testimonial(models.Model):
    client = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    comment = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['publish']
        indexes = [
            models.Index(fields=['publish'])
        ]

    def __str__(self):
        return f'{self.client} says {self.comment}'


# Project
class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='projects')
    link = models.URLField(max_length=500, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['publish']
        indexes = [
            models.Index(fields=['publish'])
        ]
    def __str__(self):
        return f'{self.title}'

