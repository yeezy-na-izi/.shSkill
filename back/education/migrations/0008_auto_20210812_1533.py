# Generated by Django 3.2.6 on 2021-08-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_auto_20210812_1524'),
    ]

    operations = [


        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(default='Пустое описание', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]