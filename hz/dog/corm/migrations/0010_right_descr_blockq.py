# Generated by Django 4.1.7 on 2023-03-05 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0009_text_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='Заголовок')),
                ('descr', models.CharField(max_length=1048, verbose_name='описание')),
                ('image', models.ImageField(upload_to='elements/', verbose_name='картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corm.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'right',
                'verbose_name_plural': 'right',
                'db_table': 'corm_right',
            },
        ),
        migrations.CreateModel(
            name='Descr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=24, verbose_name='Заголовок')),
                ('last_name', models.CharField(max_length=24, verbose_name='Заголовок-2')),
                ('descr', models.CharField(max_length=512, verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corm.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'descr',
                'verbose_name_plural': 'descr',
                'db_table': 'corm_descr',
            },
        ),
        migrations.CreateModel(
            name='BlockQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='Заголовок')),
                ('descr', models.CharField(max_length=512, verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corm.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'blockq',
                'verbose_name_plural': 'blockq',
                'db_table': 'corm_blockq',
            },
        ),
    ]
