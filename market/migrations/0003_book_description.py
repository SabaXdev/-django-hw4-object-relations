# Generated by Django 5.0.4 on 2024-04-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_book_options_alter_book_image_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
