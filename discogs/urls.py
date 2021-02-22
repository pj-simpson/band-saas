from django.urls import path

from .views import discog_page_view

urlpatterns = [
    path("", discog_page_view, name="discography"),
]