# Generated by Django 3.2.6 on 2021-08-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0023_alter_materialblocks_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='txDCsrU8eSqjuRmyPmBsYtEDg', verbose_name='Код урока'),
        ),
    ]
