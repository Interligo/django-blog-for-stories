from django.contrib import admin

from .models import Story
from .models import Comment


admin.site.register(Story)
admin.site.register(Comment)
