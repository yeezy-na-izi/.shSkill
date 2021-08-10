# Generated by Django 3.2.6 on 2021-08-07 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210807_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='coordinator',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.coordinator'),
        ),
        migrations.AlterField(
            model_name='account',
            name='student',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
        migrations.AlterField(
            model_name='account',
            name='teacher',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.teacher'),
        ),
    ]
