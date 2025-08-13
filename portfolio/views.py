from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Home Index
def index(request):    
    projects = Project.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects, 'educations':educations, 'experiences':experiences})


