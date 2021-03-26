from django.urls import path

from . import views


app_name = 'book'
urlpatterns = [
    path('about/', views.about_book, name='about_book'),
    path('content/', views.book_content, name='book_content'),
    path('<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]
