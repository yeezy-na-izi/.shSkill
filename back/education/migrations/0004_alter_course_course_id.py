# Generated by Django 3.2.6 on 2021-08-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_course_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=100, unique=True, verbose_name='Курс линк'),
        ),
    ]
