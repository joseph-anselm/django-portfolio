from django.shortcuts import render
from .models import Projects

# Create your views here.
def all_projects(request):
    projects = Projects.objects.all()
    return render (request, 'projects/all_projects.html', {'projects':projects} )