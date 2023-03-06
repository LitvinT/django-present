# Generated by Django 4.1.7 on 2023-02-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0003_alter_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about_image',
            field=models.ImageField(null=True, upload_to='about/', verbose_name='картинка-номер'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='index/', verbose_name='картинка'),
        ),
    ]
