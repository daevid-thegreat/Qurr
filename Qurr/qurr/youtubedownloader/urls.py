from django.contrib import admin
from django.urls import path
from .views import youtubedownloader, download, download_done, howtouse

app_name = 'yt_downloader'


urlpatterns = [
    path('youtube_downloader/', youtubedownloader, name='youtube downloader'),
    path('youtube_downloader/download/', download, name='download  video'),
    path('howtouse/', howtouse, name='How To Use'),
    path('download/<resolution>/', download_done, name='download_done')
    ]
