# Generated by Django 5.0 on 2024-02-02 05:42

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_cart_book_remove_cart_user_delete_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=versatileimagefield.fields.VersatileImageField(height_field='height', null=True, upload_to='profile_pics/', verbose_name='Image', width_field='width'),
        ),
    ]