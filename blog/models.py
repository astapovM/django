from PIL import Image
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    # content = models.TextField(blank=True, verbose_name="Контент")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Запись опубликована?")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse('view_blog', kwargs={"pk": self.pk})



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = "События"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
