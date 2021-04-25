from django.shortcuts import render

def news_feed_view(request):

    return render(request,'news/news_feed.html',{'nav':'news'})

def news_item_page_view(request):
    pass