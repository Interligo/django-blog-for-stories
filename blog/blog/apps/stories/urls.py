from django.urls import path

from . import views


app_name = 'stories'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:story_id>/', views.detail, name='detail'),
    path('<int:story_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]
