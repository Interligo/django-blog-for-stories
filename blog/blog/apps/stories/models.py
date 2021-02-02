from django.db import models
from django.urls import reverse


# TODO: лайки, дизлайки на комментариях; лайки на истории
class Story(models.Model):
    story_title = models.CharField('Название рассказа', max_length=200)
    story_text = models.TextField('Текст рассказа')
    story_likes = models.PositiveIntegerField(default=0)

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
