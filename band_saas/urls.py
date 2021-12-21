import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.flatpages import views


from discogs.views import home_page_view, sentry_healthcheck_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page_view, name="home"),
    path("sentry-healthcheck", sentry_healthcheck_view, name="sentry"),
    path("discog/", include("discogs.urls")),
    path("news/", include("news.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns += [
    re_path(r"^(?P<url>.*/)$", views.flatpage),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

artist = os.environ.get("ARTIST_NAME", default="Artist")
admin.site.site_header = f"{artist} Admin"
admin.site.site_title = f"{artist} Admin Dashboard"
admin.site.index_title = f"Welcome to {artist} Admin Dashboard"
