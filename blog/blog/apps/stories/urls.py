from django.urls import path

from . import views


app_name = 'stories'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:story_id>/', views.detail, name='detail'),
    path('<int:story_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('api/v1/add_story/', views.StoryCreateView.as_view(), name='add_story'),
    path('api/v1/stories_list/', views.StoriesListView.as_view(), name='stories_list'),
    path('api/v1/change_story/<int:pk>/', views.StoryChangeView.as_view(), name='change_story'),
    path('api/v1/story_detail/<int:pk>/', views.StoryDetailView.as_view(), name='story_detail'),
]
