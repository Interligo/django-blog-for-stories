import os
import sys

from django.core.wsgi import get_wsgi_application


path = '/home/Interligo/django-blog-for-stories/blog'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
application = get_wsgi_application()
