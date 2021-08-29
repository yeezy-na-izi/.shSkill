# Generated by Django 3.2.6 on 2021-08-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0035_alter_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='direction',
            field=models.CharField(choices=[('web', 'Web'), ('fb', 'Для начинающих'), ('bot', 'Боты'), ('back', 'Back'), ('front', 'Front'), ('ps', 'PhotoShop'), ('vm', 'VideoRedactor')], default='web', max_length=8, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='dgGEqnVd5VEjJp63c2UY59T7jng8HJ3U', verbose_name='Код урока'),
        ),
    ]