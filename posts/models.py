from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="post_images", blank=True, verbose_name="Картинка")
    created_at = models.DateField(auto_now=True, verbose_name="Дата создания")
    tags = models.ManyToManyField(Tag, related_name="post_tags")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
