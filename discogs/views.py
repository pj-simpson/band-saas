from django.shortcuts import render

def home_page_view(request):
    return render(request, "home.html")

def discog_page_view(request):
    return render(request,'discogs/discography.html')