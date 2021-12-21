from django.urls import path

from .views import news_feed_view, news_feed_view_fetch_more, news_item_page_view

urlpatterns = [
    path("", news_feed_view, name="news_feed"),
    path("fetch-more-news/", news_feed_view_fetch_more, name="news_feed_fetch_more"),
    path("<slug:slug>/", news_item_page_view, name="news_item_page"),
]
