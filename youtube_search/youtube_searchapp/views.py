from django.shortcuts import render,redirect
from django.conf import settings
from isodate import parse_duration
import requests
# Create your views here.

# AIzaSyAtwlTGEGOsYyuzuotVl1iDnnPfLI-6EY4

def index(request):

    videos = []

    if request.method == 'POST':

        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        
        search_params = {
            'part':'snippet',
            'q':request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults':12,
            'type':'video'
        }

       

        r = requests.get(search_url,params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {        
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part':'snippet,contentDetails',
            'id':','.join(video_ids),
            'maxResults':12
        }

        r = requests.get(video_url,params=video_params)
        results = r.json()['items']

       
        for result in results:
            # print(result)
            # print(result['snippet']['title'])
            # print(result['id'])
            # print(parse_duration(result['contentDetails']['duration']).total_seconds()//60)
            # print(result['snippet']['thumbnails']['high']['url'])

            video_data = {
                'title':result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"]}',
                'duration':int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)

    context = {
        'videos':videos
    }
    # print(videos)

    return render(request,'search/index.html',context)
