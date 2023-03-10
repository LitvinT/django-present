# Generated by Django 4.1.7 on 2023-03-06 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0013_remove_descr_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='номер')),
                ('image', models.ImageField(upload_to='elements/', verbose_name='картинка')),
                ('name', models.CharField(max_length=24, verbose_name='флаг')),
                ('visits', models.IntegerField(verbose_name='номер-посешений')),
                ('perc', models.IntegerField(verbose_name='посешения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corm.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'db_table': 'corm_countries',
            },
        ),
    ]
