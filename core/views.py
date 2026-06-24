from django.shortcuts import render

from core.models import Service, Project


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()

    context = {
        'services': services,
        'projects': projects,
    }

    return render(
        request,
        'home.html',
        context
    )
