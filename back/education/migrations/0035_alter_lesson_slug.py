# Generated by Django 3.2.6 on 2021-08-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0034_alter_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='xupb66WRTLCANwtdGay3hgXX2z7fUMqU', verbose_name='Код урока'),
        ),
    ]
