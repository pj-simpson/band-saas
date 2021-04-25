from django.contrib import admin
from django.urls import path, include

from discogs.views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_view,name="home"),
    path('discog/',include("discogs.urls")),
    path('shop/',include("shop.urls")),
    path('news/',include("news.urls")),
]
