from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'content']
	search_fields = ['title', 'content']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
	list_display = ['title', 'content']
	search_fields = ['title', 'content']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = ['title', 'content']
	search_fields = ['title', 'content']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ['client', 'role', 'comment']
	search_fields = ['client', 'role', 'comment']