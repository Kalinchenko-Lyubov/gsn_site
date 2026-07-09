# from django.urls import path
# from core.views import home, projects_gallery
#
# urlpatterns = [
#     path('', home, name='home'),
#
#     path(
#         'projects/',
#         projects_gallery,
#         name='projects_gallery'
#     ),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views  # Добавьте эту строку

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('debug-photos/', views.debug_photos, name='debug_photos'),  # Добавьте эту строку
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
