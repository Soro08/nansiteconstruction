import requests
from bs4 import BeautifulSoup
import json
url = "https://youtubemp4.to/download_ajax/"
data = {
    "url": "https://www.youtube.com/watch?v=zQOrahE-0Cs",
}
rq = requests.post(url = url, data=data)

print(rq.status_code)
#print(rq.text)
data = json.loads(rq.text)
soup = BeautifulSoup(data['result'], 'html.parser')
liens_first = soup.find(class_='results-primary')
titre = liens_first.find('h2').text
duree = liens_first.find('p').text
lientelechargement = liens_first.find("a",  attrs={'class':  "btn btn-red"})
print(titre)
print(duree)
print(lientelechargement.text, "\n" ,lientelechargement.get('href'))
#print(liens_first)
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(34 * "--")