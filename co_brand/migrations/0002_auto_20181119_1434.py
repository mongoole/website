# Generated by Django 2.1.3 on 2018-11-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='author',
            field=models.CharField(default='作者', max_length=50),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(default='标题', max_length=50),
        ),
    ]
