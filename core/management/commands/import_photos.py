import os
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Project, ProjectImage


class Command(BaseCommand):
    help = 'Import photos from folders to database'

    def handle(self, *args, **options):
        projects_dir = os.path.join(settings.MEDIA_ROOT, 'projects')

        if not os.path.exists(projects_dir):
            self.stdout.write(self.style.ERROR(f'Папка {projects_dir} не найдена'))
            return

        for folder_name in os.listdir(projects_dir):
            folder_path = os.path.join(projects_dir, folder_name)

            if not os.path.isdir(folder_path):
                continue

            # Ищем проект с таким названием
            try:
                project = Project.objects.get(title=folder_name)
            except Project.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Проект "{folder_name}" не найден в базе'))
                continue

            # Добавляем фото из папки
            photos_added = 0
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    # Создаем запись в ProjectImage
                    ProjectImage.objects.get_or_create(
                        project=project,
                        image=f'projects/{folder_name}/{file_name}'
                    )
                    photos_added += 1

            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {photos_added} фото для "{folder_name}"'
            ))