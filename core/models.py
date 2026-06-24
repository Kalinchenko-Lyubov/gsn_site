from django.db import models


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название услуги'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Project(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название объекта'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Объект'
    )

    image = models.ImageField(
        upload_to='projects/',
        verbose_name='Фотография'
    )

    def __str__(self):
        return f'{self.project.title}'

    class Meta:
        verbose_name = 'Фотография объекта'
        verbose_name_plural = 'Фотографии объектов'