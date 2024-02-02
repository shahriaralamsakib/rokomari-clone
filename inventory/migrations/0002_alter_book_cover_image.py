# Generated by Django 5.0 on 2024-02-02 05:42

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=versatileimagefield.fields.VersatileImageField(height_field='height', null=True, upload_to='book_covers/', verbose_name='Image', width_field='width'),
        ),
    ]
