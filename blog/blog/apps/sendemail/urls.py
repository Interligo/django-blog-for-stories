from django.urls import path

from . import views


app_name = 'sendemail'
urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]
