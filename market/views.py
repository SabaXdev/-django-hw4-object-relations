from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404

from market.models import Book, Author, Category


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'name': Book.name,
                'page_count': obj.page_count,
                'category': obj.category,
                'author': obj.name,
                'price': str(obj.price),
                'image': obj.image,
                'description': obj.description,
                'cover_type': obj.cover_type
            }
        elif isinstance(obj, QuerySet):
            return list(obj.values())
        return super().default(obj)


# Create your views here.
def view_of_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'all_books.html', {'page_obj': page_object})


def view_of_one_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'one_book.html', {'book': book})


def view_of_filtered_books(request):
    author_id = request.GET.get('author')
    category_id = request.GET.get('category')

    books = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()

    if author_id:
        books = books.filter(author_id=author_id)
    if category_id:
        books = books.filter(category__id=category_id)
    return render(request, 'filtered_books.html', {'books': books, 'authors': authors, 'categories': categories})
