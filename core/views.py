from django.shortcuts import render

from core.models import Service, Project, FAQ


# def home(request):
#     services = Service.objects.all()
#     projects = Project.objects.all()
#
#     context = {
#         'services': services,
#         'projects': projects,
#     }
#
#     return render(
#         request,
#         'home.html',
#         context
#     )

def projects_gallery(request):
    projects = Project.objects.prefetch_related('images').filter(show_on_projects_page=True)
    return render(request, 'projects_gallery.html', {'projects': projects})


def home(request):
    # projects = Project.objects.filter(show_on_projects_page=False)  # Только НЕ для страницы проектов
    # # или
    projects = Project.objects.all()[:3]  # Только первые 3 проекта

    faqs = FAQ.objects.filter(is_active=True)

    context = {
        'projects': projects,
        'faqs': faqs,
    }

    return render(request, 'home.html', context)