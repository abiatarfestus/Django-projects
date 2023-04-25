# Generated by Django 3.2 on 2021-05-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210509_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default='Uncategorised', related_name='posts', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='featured_image/%Y/%m/%d/', verbose_name='featured image'),
        ),
    ]
