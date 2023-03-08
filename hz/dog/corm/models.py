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
        null=True,
        blank=True
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


class Product(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='услуга',
        null=False
    )
    descr = models.CharField(
        max_length=256,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'corm_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Text(models.Model):
    name = models.CharField(
        max_length=16,
        verbose_name='Заголовок',
        null=False
    )
    descr = models.CharField(
        max_length=1048,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        db_table = 'corm_text'
        verbose_name = 'text'
        verbose_name_plural = 'text'


class Gallery(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='elements/'
    )

    class Meta:
        db_table = 'corm_gallery'
        verbose_name = 'gallery'
        verbose_name_plural = 'gallery'


class Right(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='Заголовок',
        null=False
    )
    descr = models.CharField(
        max_length=1048,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='elements/'
    )

    class Meta:
        db_table = 'corm_right'
        verbose_name = 'right'
        verbose_name_plural = 'right'


class Left(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='Заголовок',
        null=False
    )
    descr = models.CharField(
        max_length=1048,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='elements/'
    )

    class Meta:
        db_table = 'corm_left'
        verbose_name = 'left'
        verbose_name_plural = 'left'


class Descr(models.Model):
    last_name = models.CharField(
        max_length=24,
        verbose_name='Заголовок-2',
        null=False
    )
    descr = models.CharField(
        max_length=512,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        db_table = 'corm_descr'
        verbose_name = 'descr'
        verbose_name_plural = 'descr'


class BlockQ(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='Заголовок',
        null=False
    )
    descr = models.CharField(
        max_length=512,
        verbose_name='описание',
        null=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        db_table = 'corm_blockq'
        verbose_name = 'blockq'
        verbose_name_plural = 'blockq'


class Countries(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    number = models.IntegerField(
        null=False,
        verbose_name='номер'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='elements/'
    )
    name = models.CharField(
        max_length=24,
        verbose_name='флаг',
        null=False
    )
    visits = models.IntegerField(
        null=False,
        verbose_name='номер-посешений'
    )
    perc = models.IntegerField(
        null=False,
        verbose_name='посешения'
    )
    color = models.IntegerField(
        null=True,
        verbose_name='цвет'
    )

    class Meta:
        db_table = 'corm_countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Blog(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка'
    )
    day = models.IntegerField(
        verbose_name='день'
    )
    mount = models.CharField(
        max_length=16,
        verbose_name='месяц'
    )
    text = models.CharField(
        max_length=128,
        verbose_name='заголовок-текст',
        null=False
    )
    descr = models.CharField(
        max_length=512,
        verbose_name='описание',
        null=False,
    )

    class Meta:
        db_table = 'corm_blog'
        verbose_name = 'blog'
        verbose_name_plural = 'blog'


class Contact_blog(models.Model):
    email = models.EmailField(
        verbose_name='email'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'main_blog'
        verbose_name = 'blog_email_contact'
        verbose_name_plural = 'contacts'


class Blogcategory(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='имя'
    )
    count = models.IntegerField(
        verbose_name='колл'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        db_table = 'corm_blog_category'
        verbose_name = 'blog-cat'
        verbose_name_plural = 'blog-cat'


class Instagram(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='blog/'
    )
    class Meta:
        db_table = 'corm_instagram'
        verbose_name = 'instagram'
        verbose_name_plural = 'instagram'


class Recent(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='текст',
        null=False
    )
    date = models.DateField(
        verbose_name='дата'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='blog/'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    class Meta:
        db_table = 'corm_recent'
        verbose_name = 'recent'
        verbose_name_plural = 'recent'


class Posts(models.Model):
    name = models.CharField(
        max_length=12,
        verbose_name='заголовок',
        null=False
    )

    class Meta:
        db_table = 'corm_posts'
        verbose_name = 'posts'
        verbose_name_plural = 'posts'
