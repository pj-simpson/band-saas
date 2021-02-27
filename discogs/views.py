from django.shortcuts import render
from .models import Release

def home_page_view(request):
    return render(request, "home.html")

def discog_page_view(request):

    releases = Release.objects.all()
    return render(request,'discogs/discography.html',{'releases':releases})

def release_page_view(request, pk:int):
    release = Release.objects.get(id=pk)
    return render(request,"discogs/release.html",{'release':release})