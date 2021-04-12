from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main.urls')),
    path('', include('sendemail.urls')),
    path('stories/', include('stories.urls')),
    path('book/', include('book.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
