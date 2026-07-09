import os
from django.shortcuts import render
from django.conf import settings
from core.models import Project, FAQ
from django.http import JsonResponse


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


def debug_photos(request):
    """Временная страница для отладки фото"""
    result = {}

    # Проверяем MEDIA_ROOT
    result['MEDIA_ROOT'] = str(settings.MEDIA_ROOT)
    result['MEDIA_ROOT_exists'] = os.path.exists(settings.MEDIA_ROOT)

    # Проверяем projects папку
    projects_dir = os.path.join(settings.MEDIA_ROOT, 'projects')
    result['projects_dir'] = str(projects_dir)
    result['projects_dir_exists'] = os.path.exists(projects_dir)

    if os.path.exists(projects_dir):
        folders = os.listdir(projects_dir)
        result['folders_in_projects'] = folders

    # Проверяем проекты из БД
    result['projects_in_db'] = []
    for p in Project.objects.all():
        project_dir = os.path.join(settings.MEDIA_ROOT, 'projects', p.title)
        project_info = {
            'id': p.id,
            'title': p.title,
            'dir': str(project_dir),
            'exists': os.path.exists(project_dir),
        }
        if os.path.exists(project_dir):
            files = [f for f in os.listdir(project_dir) if
                     f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))]
            project_info['photos'] = files
        result['projects_in_db'].append(project_info)

    return JsonResponse(result, json_dumps_params={'ensure_ascii': False, 'indent': 2})