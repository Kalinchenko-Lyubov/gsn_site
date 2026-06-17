from django.shortcuts import render

from core.models import Service, ProjectPhoto


def home(request):
    services = Service.objects.all()
    projects = ProjectPhoto.objects.all()

    context = {
        'services': services,
        'projects': projects,
    }

    return render(
        request,
        'home.html',
        context
    )
