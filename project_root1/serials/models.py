from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Serial(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='serials_images', blank=True, null=True, verbose_name='Изображение')
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1, verbose_name='Рейтинг')
    quantity_seasons = models.PositiveIntegerField(default=1, verbose_name='Количество сезонов')
    quantity_series = models.PositiveIntegerField(default=1, verbose_name='Количество серий')
    release_year = models.PositiveIntegerField(default=1, verbose_name='Год выхода')
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_DEFAULT, default='Выберите жанр', verbose_name='Жанр')

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'

    def __str__(self):
        return self.name

    #def display_id(self):
    #    return f"{self.id:05}"
