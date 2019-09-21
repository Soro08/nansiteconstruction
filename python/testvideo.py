# importing module 
#  pip3 install certifi
import youtube_dl 
  
ydl_opts = {} 
  
def dwl_vid(): 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        ydl.download([zxt]) 
  
channel = 1
while (channel == int(1)): 
    link_of_the_video = "https://www.youtube.com/watch?v=Wz86pFtHZqI"
    zxt = link_of_the_video.strip() 
  
    dwl_vid() 
    channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done ")) 
