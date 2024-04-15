# Generated by Django 5.0.4 on 2024-04-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_book_author_name_alter_book_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.CharField(blank=True, choices=[('hard', 'Hard'), ('soft', 'Soft'), ('special', 'Special')], max_length=7, null=True, verbose_name='Book Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(help_text='Enter the name of the author', max_length=255, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(help_text='Enter the category of the book', max_length=255, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='', help_text='Enter a description of the book', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(help_text='Enter the name of the book', max_length=255, null=True, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Enter the price of the book', max_digits=6, null=True, verbose_name='Price'),
        ),
    ]
