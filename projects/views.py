from .models import Person, Project
from django.shortcuts import render

def search(request):
    query = request.GET.get('q')
    people = Person.objects.filter(name__icontains=query)
    projects = Project.objects.filter(name__icontains=query)
    context = {
        "people": people,
        "projects": projects
    }
    return render(request, "projects/search.html", context)


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def person_list(request):
    people = Person.objects.all()
    context = {
        "people": people
    }
    return render(request, "projects/person_list.html", context)


def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    context = {
        'person': person
    }
    return render(request, 'projects/person_detail.html', context)

