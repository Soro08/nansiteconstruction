from youtube_api import YouTubeDataAPI

api_key = 'AIzaSyBzxH8kNtZw5-p0otDM4YwAXBl0HaNEpEM'
yt = YouTubeDataAPI(api_key)

searches = yt.search(q='dj arafat',max_results=1,parser=None)
pl = yt.get_videos_from_playlist_id(playlist_id='PLCiKBmAOYVNesZUUnBZB22P6CCpO70tDC', next_page_token=None,  part=['snippet'])
print(pl)