# Generated by Django 5.1.3 on 2024-11-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
    ]
