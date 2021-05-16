from django.shortcuts import render
from django.core.paginator import Paginator

from news.models import NewsItem

def news_feed_view(request):
    news_items = NewsItem.objects.all().order_by('created')
    paginator = Paginator(news_items, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'news/news_feed.html',{'news_items':page_obj,'nav':'news'})

def news_item_page_view(request,slug:str):
    news_item = NewsItem.objects.get(slug=slug)
    return render(request, 'news/news_item.html', {'news_item': news_item, 'nav': 'news'})

