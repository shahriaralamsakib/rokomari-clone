# Generated by Django 5.0 on 2024-01-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('published_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
