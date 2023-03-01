from django.db import models
from django.utils.timezone import now


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
        verbose_name='картинка',

    )
    about_image = models.ImageField(
        upload_to='about/',
        verbose_name='картинка-номер',
        null=True
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


class Comment(models.Model):
    name = models.CharField(
        max_length=16,
        verbose_name='имя'
    )
    permission = models.CharField(
        max_length=32,
        verbose_name='должность'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='описание'
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
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )


class Contact(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='name'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message = models.CharField(
        max_length=1024,
        verbose_name='message'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date created'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'main_contacts'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['date_created']