from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Запись опубликовано?")


    def __str__(self):
        return self.title


    class Meta():
        verbose_name = 'Событие'
        verbose_name_plural = "События"
        ordering = ['-created_at']
