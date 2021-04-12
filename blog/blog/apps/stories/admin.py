from django.contrib import admin

from .models import Story
from .models import Comment


@admin.register(Story)
class PostAdmin(admin.ModelAdmin):
    list_display = ('story_title', 'story_competition', 'story_award_winning_place')
    list_filter = ('story_title',)
    search_fields = ('story_title',)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('story', 'authors_name', 'comment_text', 'publication_date')
    list_filter = ('authors_name', 'publication_date')
    search_fields = ('authors_name',)
