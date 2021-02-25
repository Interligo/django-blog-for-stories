from django.urls import path

from . import views


app_name = 'book'
urlpatterns = [
    path('', views.about_book, name='about_book'),
    path('<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]
