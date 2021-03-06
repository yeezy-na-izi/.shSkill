# Generated by Django 3.2.6 on 2021-08-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0039_alter_lesson_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('category_id', models.IntegerField()),
                ('brand_id', models.IntegerField()),
                ('shows', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('orders', models.IntegerField()),
                ('gmv', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Удали',
                'verbose_name_plural': 'Удали',
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='ChtjXwQt6CvK4vrGDDKWcWHwCByrP6eS', unique=True, verbose_name='Код урока'),
        ),
    ]
