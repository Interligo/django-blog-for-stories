from django.db import models


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

    def pretty_description_print(self) -> list:
        text_to_split = str(self.book_description)
        return text_to_split.split('\n')


class BookChapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    chapter_title = models.CharField('Название главы', max_length=200)
    chapter_text = models.TextField('Текст главы', blank=True)

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
        ordering = ('id',)

    def __str__(self):
        return f'{self.book}: {self.chapter_title}'

    def __repr__(self):
        return self.chapter_title

    def get_chapter_ids_list(self) -> list:
        """Return all book chapters list."""
        chapter_ids_list = []

        chapters = self.book.chapters.all()
        for chapter in chapters:
            chapter_ids_list.append(chapter.id)

        return chapter_ids_list

    def get_first_chapter(self) -> int:
        """Return first chapters number."""
        chapter_ids = self.get_chapter_ids_list()
        return min(chapter_ids)

    def get_last_chapter(self) -> int:
        """Return last chapters number."""
        chapter_ids = self.get_chapter_ids_list()
        return max(chapter_ids)

    def get_previous_chapter(self) -> int:
        """For navigating between chapters. Return previous chapter's number."""
        current_chapter, previous_chapter = self.id, 0
        first_chapter = self.get_first_chapter()

        if current_chapter == first_chapter:
            previous_chapter = first_chapter
        else:
            previous_chapter = current_chapter - 1

        return previous_chapter

    def get_next_chapter(self) -> int:
        """For navigating between chapters. Return next chapter's number."""
        current_chapter, next_chapter = self.id, 0
        last_chapter = self.get_last_chapter()

        if current_chapter >= last_chapter:
            next_chapter = last_chapter
        else:
            next_chapter = current_chapter + 1

        return next_chapter

    def pretty_chapter_print(self) -> list:
        text_to_split = str(self.chapter_text)
        return text_to_split.split('\n')
