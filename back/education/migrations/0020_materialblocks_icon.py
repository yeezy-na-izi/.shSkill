# Generated by Django 3.2.6 on 2021-08-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0019_auto_20210821_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialblocks',
            name='icon',
            field=models.CharField(choices=[('fa-bolt', 'Молния')], default='fa-bolt', max_length=16),
        ),
    ]