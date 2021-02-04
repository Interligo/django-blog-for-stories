from django.db import models


# TODO: Сделать корректный счетчик просмотров
class PageHit(models.Model):
    url = models.CharField(unique=True, max_length=2000)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Счётчик'
        verbose_name_plural = 'Счётчики'

    def __str__(self):
        return f'Счётчик {self.url}, {str(self.count)} просмотров.'
