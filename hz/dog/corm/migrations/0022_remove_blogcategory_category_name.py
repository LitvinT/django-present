# Generated by Django 4.1.7 on 2023-03-08 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0021_remove_blog_item_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='category_name',
        ),
    ]
