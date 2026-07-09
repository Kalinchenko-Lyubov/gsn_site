from django.urls import path

from core import views
from core.views import home, projects_gallery

# urlpatterns = [
#     path('', home, name='home'),
#
#     path(
#         'projects/',
#         projects_gallery,
#         name='projects_gallery'
#     ),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_gallery, name='projects_gallery'),
    path('debug-photos/', views.debug_photos, name='debug_photos'),  # Добавьте эту строку
]