# Generated by Django 3.2.6 on 2021-08-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0033_auto_20210829_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='PPCcTYukAcu6qChcVeCX8arDCYyCYHu6', verbose_name='Код урока'),
        ),
    ]
