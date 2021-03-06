# Generated by Django 3.2.6 on 2021-08-09 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_student_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Tech', 'Технический Администратор'), ('Course', 'Администратор Курса'), ('World', 'Всемирный Администратор')], max_length=6, verbose_name='role')),
            ],
            options={
                'verbose_name': 'Администратор',
                'verbose_name_plural': 'Администратор',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='description',
        ),
        migrations.AddField(
            model_name='account',
            name='administrator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.administrator'),
        ),
    ]
