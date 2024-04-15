from django.contrib import admin
from market.models import Book, Author, Category


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_count', 'author', 'price', 'cover_type')
    search_fields = ('name', 'author')
    list_filter = ('author_name', 'category', 'book_cover')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
