from django.urls import path

from .views import news_feed_view, news_item_page_view

urlpatterns = [
    path("", news_feed_view, name="news_feed"),
    path("<slug:slug>/", news_item_page_view, name="news_item_page"),
]
