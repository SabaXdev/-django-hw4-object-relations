from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(null=True, max_length=255, verbose_name=_('Book Name'), help_text=_('Enter the name of the book'))
    page_count = models.IntegerField(null=True, blank=True, verbose_name=_('Page Count'), help_text=_('Enter the number of pages in the book'))
    category = models.ManyToManyField(to="Category", verbose_name=_('Category'), help_text=_('Enter the category of the book'))
    author = models.ForeignKey(to="Author", on_delete=models.CASCADE, verbose_name=_('Author Name'), help_text=_('Enter the name of the author'))
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2, verbose_name=_('Price'), help_text=_('Enter the price of the book'))
    image = models.ImageField(null=True, blank=True, upload_to='books/', verbose_name=_('Image'), help_text=_('Upload an image of the book cover'))
    description = models.TextField(null=True, default='', verbose_name=_('Description'), help_text=_('Enter a description of the book'))
    cover_type = models.CharField(max_length=7, choices=(('hard', 'Hard'), ('soft', 'Soft'), ('special', 'Special')), null=True, blank=True, verbose_name=_('Cover Type'))

    def __str__(self):
        return f"{self.name} by {self.author}"

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Author Name'), help_text=_('Enter the name of the author'))

    def __str__(self):
        return f"Author is {self.name}"

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Category Name'), help_text=_('Enter the category of the book'))

    def __str__(self):
        return f"Category is {self.name}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
