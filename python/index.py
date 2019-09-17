import urllib.request

url_link = 'https://www.youtube.com/watch?v=_oy-J9-j2mM'


import youtube_dl
import os

ydl_opts = {}
#
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])