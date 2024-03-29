from django.db import models


class PageHit(models.Model):
    """Class for a page's visiting count."""
    url = models.CharField(unique=True, max_length=2000)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Счётчик'
        verbose_name_plural = 'Счётчики'

    def __str__(self):
        return f'Счётчик {self.url}, {str(self.count)} просмотров.'
