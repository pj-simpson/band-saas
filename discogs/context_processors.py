import os

def site_artist_name(request):
    artist = os.environ.get("ARTIST_NAME",default='Artist')
    return {'artist':artist}