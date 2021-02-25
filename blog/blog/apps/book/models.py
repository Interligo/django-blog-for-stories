from django.db import models
from django.shortcuts import get_object_or_404


class Book(models.Model):
    book_title = models.CharField('Название книги', max_length=200)
    book_description = models.TextField('Описание книги', blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.book_title

    def __repr__(self):
        return self.book_title


class BookChapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    chapter_title = models.CharField('Название главы', max_length=200)
    chapter_text = models.TextField('Текст главы', blank=True)

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return f'{self.book}: {self.chapter_title}'

    def __repr__(self):
        return self.chapter_title

    # def get_all_chapters(self):
    #     book = get_object_or_404(Book, id=self.book.id)
    #     chapters = book.chapters.order_by('id')
    #     return chapters

    # def get_chapter_ids(self):
    #     book = get_object_or_404(Book, id=1)
    #     chapters = book.chapters.order_by('id')
    #     result = {}
    #
    #     for chapter in chapters:
    #         result[chapter] = chapter.id
    #
    #     return result
