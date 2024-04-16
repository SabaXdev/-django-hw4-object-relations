from django.contrib import admin
from market.models import Book, Author, Category


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'page_count', 'price', 'cover_type')
    search_fields = ('name', 'author')
    list_filter = ('author', 'category', 'cover_type')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
