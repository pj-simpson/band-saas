from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from discogs.views import home_page_view

urlpatterns = [
    path('info/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    path('',home_page_view,name="home"),
    path('discog/',include("discogs.urls")),
    path('shop/',include("shop.urls")),
    path('news/',include("news.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

