# Generated by Django 3.2.6 on 2021-08-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_group_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(default='qwe', max_length=100, verbose_name='Курс линк'),
            preserve_default=False,
        ),
    ]
