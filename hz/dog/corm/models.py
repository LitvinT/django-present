from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='category'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'corm_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Team(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='имя'
    )
    title = models.CharField(
        max_length=16,
        verbose_name='должность'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    image = models.ImageField(
        upload_to='index/',
        verbose_name='картинка'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'corm_team'
        verbose_name = 'команда'
        verbose_name_plural = 'команда'