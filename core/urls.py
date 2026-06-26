from django.urls import path

from core.views import home, projects_gallery

urlpatterns = [
    path('', home, name='home'),

    path(
        'projects/',
        projects_gallery,
        name='projects_gallery'
    ),
]