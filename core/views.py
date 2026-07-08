import os
from django.shortcuts import render
from django.conf import settings
from core.models import Service, Project, FAQ


def projects_gallery(request):
    projects = Project.objects.prefetch_related('images').filter(show_on_projects_page=True)

    # Добавляем фото для каждого проекта
    project_photos = {}
    for project in projects:
        project_dir = os.path.join(settings.MEDIA_ROOT, 'projects', project.title)
        if os.path.exists(project_dir):
            photos = []
            for file in os.listdir(project_dir):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    photos.append(f'projects/{project.title}/{file}')
            project_photos[project.title] = photos

    return render(request, 'projects_gallery.html', {
        'projects': projects,
        'project_photos': project_photos,
    })


def home(request):
    projects = Project.objects.all()[:3]  # Только первые 3 проекта

    # Добавляем фото для главной
    project_photos = {}
    for project in projects:
        project_dir = os.path.join(settings.MEDIA_ROOT, 'projects', project.title)
        if os.path.exists(project_dir):
            photos = []
            for file in os.listdir(project_dir):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    photos.append(f'projects/{project.title}/{file}')
            project_photos[project.title] = photos

    faqs = FAQ.objects.filter(is_active=True)

    context = {
        'projects': projects,
        'project_photos': project_photos,
        'faqs': faqs,
    }

    return render(request, 'home.html', context)