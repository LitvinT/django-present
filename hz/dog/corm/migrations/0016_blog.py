# Generated by Django 4.1.7 on 2023-03-08 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0015_countries_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='картинка')),
                ('day', models.DateTimeField(verbose_name='день')),
                ('mount', models.DateTimeField(verbose_name='месяц')),
                ('text', models.CharField(max_length=128, verbose_name='заголовок-текст')),
                ('descr', models.CharField(max_length=512, verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corm.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blog',
                'db_table': 'corm_blog',
            },
        ),
    ]
