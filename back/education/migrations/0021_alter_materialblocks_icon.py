# Generated by Django 3.2.6 on 2021-08-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0020_materialblocks_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialblocks',
            name='icon',
            field=models.CharField(choices=[('bolt', 'Молния'), ('apple-alt', 'Яблоко'), ('balance-scale-left', 'Весы'), ('brain', 'Мозг'), ('check', 'Галочка'), ('cloud', 'Облако'), ('compass', 'Компас'), ('dev', 'dev'), ('git', 'git'), ('git', 'git')], default='fa-bolt', max_length=32),
        ),
    ]
