# Generated by Django 4.2.6 on 2023-11-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_items_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_img',
            field=models.ImageField(default=None, upload_to='static/images/'),
        ),
    ]
