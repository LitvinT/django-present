# Generated by Django 4.1.7 on 2023-02-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='публикация'),
        ),
    ]
