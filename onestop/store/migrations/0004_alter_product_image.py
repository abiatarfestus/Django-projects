# Generated by Django 4.0.1 on 2022-03-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_description_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_pics/placeholder.png', upload_to='product_pics'),
        ),
    ]
