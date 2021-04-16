from django.contrib import admin

from book.models import Book
from book.models import BookChapter


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ('book_title',)
    list_filter = ('book_title',)
    search_fields = ('book_title',)


@admin.register(BookChapter)
class PostAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapter_title')
    list_filter = ('book', 'chapter_title')
    search_fields = ('book',)
