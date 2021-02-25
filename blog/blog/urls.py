from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('', include('main.urls')),
    path('', include('sendemail.urls')),
    path('stories/', include('stories.urls')),
    path('book/', include('book.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
