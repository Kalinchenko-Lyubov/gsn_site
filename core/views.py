from django.shortcuts import render

from core.models import Service, Project, FAQ


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

def projects_gallery(request):

    projects = Project.objects.all()

    return render(
        request,
        'projects_gallery.html',
        {
            'projects': projects
        }
    )


def home(request):
    projects = Project.objects.all()  # Получаем все проекты
    faqs = FAQ.objects.filter(is_active=True)  # Получаем активные FAQ

    context = {
        'projects': projects,
        'faqs': faqs,
    }

    return render(request, 'home.html', context)