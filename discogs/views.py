from django.shortcuts import render
from .models import Release

def home_page_view(request):
    return render(request, "home.html",{'nav':'home'})

def discog_page_view(request):

    releases = Release.objects.all()
    return render(request,'discogs/discography.html',{'releases':releases, 'nav':'discog'})

def release_page_view(request, slug:str):
    release = Release.objects.get(slug=slug)
    return render(request,"discogs/release.html",{'release':release, 'nav':'discog'})