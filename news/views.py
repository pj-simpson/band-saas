from django.shortcuts import render

from news.models import NewsItem

def news_feed_view(request):
    news_items = NewsItem.objects.all()
    return render(request,'news/news_feed.html',{'news_items':news_items,'nav':'news'})

def news_item_page_view(request,slug:str):
    news_item = NewsItem.objects.get(slug=slug)
    return render(request, 'news/news_item.html', {'news_item': news_item, 'nav': 'news'})
