# Generated by Django 3.2.6 on 2021-08-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_course_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ended',
            field=models.BooleanField(default=False, verbose_name='Закончена'),
        ),
    ]
