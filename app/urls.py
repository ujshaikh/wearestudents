"""
URL configuration for wearestudents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static  # Import static

urlpatterns = [
    path('', include('tenurdu.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    path('ads.txt', serve, {'document_root': settings.BASE_DIR, 'path': 'ads.txt'}, name='ads_txt'),
    path('sitemap.xml', serve, {'document_root': settings.BASE_DIR, 'path': '/tenurdu/sitemap.xml'}, name='sitemap_xml'),
    path('robots.txt', serve, {'document_root': settings.BASE_DIR, 'path': '/tenurdu/robots.txt'}, name='robots_txt'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)