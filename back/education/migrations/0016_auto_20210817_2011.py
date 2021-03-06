# Generated by Django 3.2.6 on 2021-08-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0015_course_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('block', models.FileField(upload_to='static/education/course/', verbose_name='Информация блока')),
            ],
            options={
                'verbose_name': 'Блок материала',
            },
        ),
        migrations.RemoveField(
            model_name='material',
            name='file',
        ),
        migrations.AddField(
            model_name='material',
            name='annotations',
            field=models.TextField(blank=True, verbose_name='Аннотация'),
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='materials',
        ),
        migrations.AddField(
            model_name='lesson',
            name='materials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.material', verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='material',
            name='blocks',
            field=models.ManyToManyField(blank=True, to='education.MaterialBlocks', verbose_name='Блоки'),
        ),
    ]
