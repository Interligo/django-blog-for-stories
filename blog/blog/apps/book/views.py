from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book
from .models import BookChapter


def about_book(request, book_id=1):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/about_book.html', {'book': book})


def book_content(request, book_id=1):
    book = get_object_or_404(Book, id=book_id)
    chapters = book.chapters.order_by('id')
    return render(request, 'book/book_content.html', {'book': book, 'chapters': chapters})


def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(BookChapter, id=chapter_id)
    return render(request, 'book/chapter_detail.html', {'chapter': chapter})
