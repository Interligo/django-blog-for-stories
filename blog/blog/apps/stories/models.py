from django.db import models


class Story(models.Model):
    story_title = models.CharField('Название рассказа', max_length=200)
    story_text = models.TextField('Текст рассказа', blank=True)
    story_competition = models.CharField('Название конкурса', max_length=200, default='Неизвестно')
    story_competition_description = models.CharField('Описание конкурса', max_length=500, default='Неизвестно')
    story_award_winning_place = models.CharField('Призовое место', max_length=10, default='Неизвестно')

    class Meta:
        verbose_name = 'Рассказ'
        verbose_name_plural = 'Рассказы'

    def __str__(self):
        return self.story_title


class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    authors_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    publication_date = models.DateTimeField('Дата публикации комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.authors_name}: {self.comment_text}'
