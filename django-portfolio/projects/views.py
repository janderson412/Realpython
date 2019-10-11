from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse

# Create your views here.

#def project_list(request):
    #return render(request, 'projects/index.html')

def all_projects(request):
    # query DB to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})

