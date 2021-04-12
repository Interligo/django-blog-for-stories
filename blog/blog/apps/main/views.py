from django.shortcuts import render


def index(request):
    """For render site's main page."""
    return render(request, 'main/main_page.html')
