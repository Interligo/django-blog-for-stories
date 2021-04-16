from django.shortcuts import render
from django.shortcuts import get_object_or_404

from book.models import Book
from book.models import BookChapter


def about_book(request, book_id=1):
    """For book's description page. Site contains only one book, so book_id value == 1 is default."""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/about_book.html', {'book': book})


def book_content(request, book_id=1):
    """For book's content page. Site contains only one book, so book_id value == 1 is default."""
    book = get_object_or_404(Book, id=book_id)
    chapters = book.chapters.order_by('id')
    return render(request, 'book/book_content.html', {'book': book, 'chapters': chapters})


def chapter_detail(request, chapter_id):
    """For current chapter render."""
    chapter = get_object_or_404(BookChapter, id=chapter_id)
    return render(request, 'book/chapter_detail.html', {'chapter': chapter})
