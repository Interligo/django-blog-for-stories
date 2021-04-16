from django.urls import path
from django.urls import include

from . import views


app_name = 'api'
urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('stories/', views.StoriesListView.as_view(), name='stories_list'),
    path('stories/<int:pk>/', views.StoryChangeView.as_view(), name='change_story'),
    path('stories/add/', views.StoryCreateView.as_view(), name='add_story'),
]


