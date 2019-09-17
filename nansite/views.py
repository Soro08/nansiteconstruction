from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
# Create your views here.
def home(request):
    return render(request, 'index.html')

def youtubes(request):
    return render(request, 'yout.html')

def getlink(request):
    key = json.loads(request.body.decode('utf-8'))

    lien = key['liens']
    print(lien)
    url = "https://youtubemp4.to/download_ajax/"
    data = {
        "url": "https://www.youtube.com/watch?v=bFEP26jCtsQ",
    }
    rq = requests.post(url = url, data=data)
    datas = json.loads(rq.text)
    return JsonResponse(datas, safe=False)